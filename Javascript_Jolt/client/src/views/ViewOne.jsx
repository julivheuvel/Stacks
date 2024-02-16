import { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

const ViewOne = (props) => {

   const { id } = useParams();
   console.log(id)

   const [oneCoffee, setOneCoffee] = useState({})



   useEffect(() => {

      axios.get(`http://localhost:8000/api/coffee/${id}`)
         .then( res => {
            console.log(res.data)
            setOneCoffee(res.data)
         })
         .catch(err => console.log("error getting info from useEffect", err))
   
   }, [id])


   return (
      <div>
         {
            oneCoffee ? (
               <div>
                  <p>Coffee: {oneCoffee.name}</p>
                  
                  <p>Description: {oneCoffee.description}</p>
                  <p>Roast: {oneCoffee.roast}</p>
                  <p>Price: ${oneCoffee.price}</p>
                  {oneCoffee.decalf ? <p>Decalf</p> : <p>Caffeinated</p>}
               </div>
            ) : <h3>loading...</h3>
         }
      </div>
   )
}

export default ViewOne;