import {model, Schema} from "mongoose";

const CoffeeSchema = new Schema({
    name: {
        type: String,
        required: [true, "Name is required!"],
        minlength: [2, "Must have at least 2 characters"]
    },
    description: {
        type: String,
        required: [true, "{PATH} is required!"],
        minlength: [2, "Must have at least 2 characters"]
    },
    roast: {
        type: String,
        required: [true, "{PATH} is required!"],
        minlength: [2, "Must have at least 2 characters"]
    },
    price: {
        type: Number,
        required: [true, "{PATH} is required!"]
    },
    decalf:{
        type: Boolean,
        default: false
    } 
}, {timestamps: true});

export default model("Coffee", CoffeeSchema);