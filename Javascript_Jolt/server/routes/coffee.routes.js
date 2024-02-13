import { Router } from "express";
const router = Router();
import coffeeController from "../controllers/coffee.controller.js";

router.route("/coffee")
    .get(coffeeController.readAll)
    .post(coffeeController.create);

router.route("/coffee/:id")
    .get(coffeeController.viewOne)
    .put(coffeeController.update)
    .delete(coffeeController.delete);


export default router;