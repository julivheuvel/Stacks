import { useState, useEffect } from "react";
import axios from "axios";
import { Link } from 'react-router-dom';

function Home() {
  // set to array becauase res.data from line 14 returns an array
   const [coffee, setCoffee] = useState([]);

   useEffect(() => {
      axios
      .get("http://localhost:8000/api/coffee")
      .then((res) => {
         console.log(res.data);
         setCoffee(res.data);
      })
      .catch((err) => console.log("error with axios call", err));
   }, []);   

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
            </tr>
         </thead>
         <tbody>
            {
               coffee.map(c => {
                  return (
                     <tr key={c._id}>
                        <td>
                           <Link to={`/coffee/${c._id}`}>
                              {c.name}
                           </Link>
                        </td>
                        <td>{c.description}</td>
                        <td>{c.roast}</td>
                        <td>{c.price}</td>
                        {c.decalf ? <td>Decalf</td> : <td>Caffeinated</td>}
                        
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
