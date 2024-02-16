import { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams, useNavigate} from 'react-router-dom';

const Edit = (props) => {

    
   const navigate = useNavigate();

    const { id } = useParams();
    console.log(id)

    const [oneCoffee, setOneCoffee] = useState({
        name: "",
        description: "",
        roast: "",
        price: "",
        decalf: ""
    })


    // const [form, setForm] = useState({});
    const [formError, setFormError] = useState({});

    
    useEffect(() => {
        
        axios.get(`http://localhost:8000/api/coffee/${id}`)
            .then( res => {
                console.log(res.data)
                setOneCoffee(res.data)
            })
            .catch(err => console.log("error getting info from useEffect", err))
    }, [id])
    
    const onChangeHandler = (event) => {
        setOneCoffee({
            ...oneCoffee,
            [event.target.name]:event.target.value
        })
    }

    const onUpdateHandler = (event) => {
        event.preventDefault();
        console.log("at the onUpdateHandler")
        // console.log(form)
        axios.put(`http://localhost:8000/api/coffee/${id}`, oneCoffee)
            .then(res => {
                console.log(res.data)
                // go to recently created coffee
                navigate("/coffee/" + oneCoffee._id);
            })
            .catch(err => {
                console.log("hereee")
                console.log(err.response.data.error.errors)
                console.log("Error with creation", err.response.data.error.errors)
                setFormError(err.response.data.error.errors)
            })
    
        };

    return (

        <div>
            <h1>Update Coffee</h1>

            <form onSubmit={onUpdateHandler}>
                <div className="form-group mb-3">
                    {formError.name ? <p className="text-danger">{formError.name.message}</p> : ""}

                    <label>Name:</label>
                    <input type="text" className="form-control" value={oneCoffee.name} name="name" onChange={onChangeHandler} />
                </div>
                <div className="form-group mb-3">
                    {formError.description ? <p className="text-danger">{formError.description.message}</p> : ""}

                    <label>Description:</label>
                    <input type="text" className="form-control" value={oneCoffee.description} name="description" onChange={onChangeHandler} />
                </div>
                
                <div className="form-group mb-3">
                    {formError.roast ? <p className="text-danger">{formError.roast.message}</p> : ""}

                    <label>Roast:</label>
                    <input type="text" className="form-control" name="roast" value={oneCoffee.roast} onChange={onChangeHandler} />
                </div>
                <div className="form-group mb-3">
                    {formError.price ? <p className="text-danger">{formError.price.message}</p> : ""}

                    <label>Price:</label>
                    <input type="number" className="form-control" name="price" value={oneCoffee.price} onChange={onChangeHandler} />
                </div>
                <div className="form-group mb-3 d-flex justify-content-center gap-4">
                        {formError.decalf ? <p className="text-danger">{formError.decalf.message}</p> : ""}

                        {
                            oneCoffee.decalf ? 
                                <div>
                                    <div className="d-flex justify-content-center gap-2">
                                        <label>Decalf:</label>
                                        <input type="radio" className="form-check-input" checked name="decalf"  onChange={onChangeHandler}/>
                                    </div>

                                    <div className="d-flex justify-content-center gap-2">
                                        <label>Caffeinated:</label>
                                        <input type="radio" className="form-check-input" name="decalf" value="false" onChange={onChangeHandler}/>
                                    </div>
                                </div>
                                : 
                                <div>
                                    <div className="d-flex justify-content-center gap-2">
                                        <label>Decalf:</label>
                                        <input type="radio" className="form-check-input" name="decalf"  onChange={onChangeHandler}/>
                                    </div>

                                    <div className="d-flex justify-content-center gap-2">
                                        <label>Caffeinated:</label>
                                        <input type="radio" className="form-check-input" checked name="decalf" value="false" onChange={onChangeHandler}/>
                                    </div>
                                </div>
                        }

                        
                </div>
                <input type="submit" value="Update it!" className="btn btn-success shadow mt-3" />
            </form>
        </div>
    )
}

export default Edit;