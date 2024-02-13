// import model using ESM to query
import Coffee from "../models/coffee.model.js";

const coffeeController = {

    // ============
    // CREATE
    // ============
    create : async (req, res) => {
        try {
            const newCoffee = await Coffee.create(req.body);
            res.json(newCoffee);
        }
        catch (error) {
            console.log(error);
            res.status(400).json({message:"error creating new coffee", error: error});
        }
    },

    // ============
    // READ ALL
    // ============
    readAll : async (req, res) => {
        try {
            const allCoffee = await Coffee.find();
            res.json(allCoffee)
        }
        catch (error) {
            console.log( error);
            res.status(400).json({message: "error getting all coffee", error: error});
        }
    },

    // ============
    // VIEW ONE
    // ============

    viewOne : async (req, res) => {
        try {
            const oneCoffee = await Coffee.findById(req.params.id);
            res.json(oneCoffee);
        }
        catch (error) {
            console.log(error);
            res.status(400).json({message: "error finding one coffee", error: error});
        }
    },


    // ============
    // UPDATE ONE
    // ============
    update : async (req, res) => {
        // if updating validate then return new object
        const options = {
            new: true,
            runValidators: true,
        };

        try {
            const updatedCoffee = await Coffee.findByIdAndUpdate(req.params.id, req.body, options);
            res.json(updatedCoffee);
        }
        catch (error) {
            console.log(error);
            res.status(400).json({message: "error updating coffee!", error: error});
        }
    },


    // ============
    // DELETE ONE
    // ============
    delete : async (req, res) => {
        try {
            const deletedCoffee = await Coffee.findByIdAndDelete(req.params.id);
            res.json(deletedCoffee);
        }
        catch (error) {
            console.log(error);
            res.status(400).json({message: "error trying to delete this coffee!", error: error});
        }
    }
};

export default coffeeController;