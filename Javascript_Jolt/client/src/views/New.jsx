import { useState } from "react";
import axios from "axios";
import { Navigate, useNavigate } from "react-router-dom";

const New = (props) => {

   const navigate = useNavigate();

   const [form, setForm] = useState({});
   const [formError, setFormError] = useState({});

   const onChangeHandler = (event) => {
      setForm({
         ...form,
         [event.target.name]:event.target.value
      })
   }

   const onSubmitHandler = (event) => {
      event.preventDefault();
      console.log("at the onSubmitHandler")
      // console.log(form)
      axios.post("http://localhost:8000/api/coffee", form)
         .then(res => {
            console.log(res.data)
            // go to recently created coffee
            navigate("/coffee/" + res.data._id);
         })
         .catch(err => {
            console.log("hereee")
            console.log(err.response.data)
            console.log("Error with creation", err.response.data.error.errors)
            setFormError(err.response.data.error.errors)
         })

   };

   return (
   
      <div>
         
         <h1>Create New Coffee</h1>

         <form onSubmit={onSubmitHandler}>
            <div className="form-group mb-3">
               {formError.name ? <p className="text-danger">{formError.name.message}</p> : ""}

               <label>Name:</label>
               <input type="text" className="form-control" name="name" onChange={onChangeHandler} />
            </div>
            <div className="form-group mb-3">
               {formError.description ? <p className="text-danger">{formError.description.message}</p> : ""}

               <label>Description:</label>
               <input type="text" className="form-control" name="description" onChange={onChangeHandler} />
            </div>
            
            <div className="form-group mb-3">
               {formError.roast ? <p className="text-danger">{formError.roast.message}</p> : ""}

               <label>Roast:</label>
               <input type="text" className="form-control" name="roast" onChange={onChangeHandler} />
            </div>
            <div className="form-group mb-3">
               {formError.price ? <p className="text-danger">{formError.price.message}</p> : ""}

               <label>Price:</label>
               <input type="number" className="form-control" name="price" onChange={onChangeHandler} />
            </div>
            <div className="form-group mb-3 d-flex justify-content-center gap-4">
                  {formError.decalf ? <p className="text-danger">{formError.decalf.message}</p> : ""}

                  <div className="d-flex justify-content-center gap-2">
                     <label>Decalf:</label>
                     <input type="radio" className="form-check-input" name="decalf" value="true" onChange={onChangeHandler}/>
                  </div>

                  <div className="d-flex justify-content-center gap-2">
                     <label>Caffeinated:</label>
                     <input type="radio" checked className="form-check-input" name="decalf" value="false" onChange={onChangeHandler}/>
                  </div>
            </div>
            <input type="submit" value="Add it!" className="btn btn-success shadow mt-3" />
         </form>

      </div>
   
   );
};

export default New;
