import { useState, useEffect } from "react";
import axios from "axios";
import { Link, useNavigate } from 'react-router-dom';

const Home = () => {
   const navigate = useNavigate();
  // set to array becauase res.data from line 14 returns an array
   const [coffee, setCoffee] = useState([]);
   const [deleted, setDeleted] = useState(false)

   useEffect(() => {
      axios.get("http://localhost:8000/api/coffee")
      .then((res) => {
         console.log(res.data);
         setCoffee(res.data);
      })
      .catch((err) => console.log("error with axios call", err));
   }, []);   


   const goToEdit = (id) => {
      navigate("/coffee/edit/" + id)
   }

   const onDeleteHandler = (event, id) => {
      console.log("delete")

      axios.delete(`http://localhost:8000/api/coffee/${id}`)
         .then(res => {
            console.log(res.data)
            setDeleted(!deleted)
            navigate("/coffee")
         })
         .catch(err => console.log("Error deleting coffee", err));
   }

   return (
      <div>
      <h1>All Coffee</h1>

      {/* <p>{JSON.stringify(coffee)}</p> */}

      <table>
         <thead>
            <tr>
            <th>Name</th>
            <th>Description</th>
            <th>Roast</th>
            <th>Price</th>
            <th>Decalf</th>
            <th>Actions</th>
            </tr>
         </thead>
         <tbody>
            {
               coffee.map(c => {
                  return (
                     <tr key={c._id} className="">
                        <td>
                           <Link to={`/coffee/${c._id}`}>
                              {c.name}
                           </Link>
                        </td>
                        <td>{c.description}</td>
                        <td>{c.roast}</td>
                        <td>{c.price}</td>
                        {c.decalf ? <td>Decalf</td> : <td>Caffeinated</td>}
                        <td className="d-flex justify-content-center align-items-center gap-2">
                           <button className="btn btn-outline-dark" onClick={() => goToEdit(c._id)}>Edit</button>
                           <button className="btn btn-outline-danger" onClick={(event) => onDeleteHandler(event, c._id)}>Delete</button>
                        </td>
                        
                     </tr>     
                  );
               })
            }
         </tbody>
      </table>
      </div>
   );
}

export default Home;
