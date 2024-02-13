import { connect } from 'mongoose';
import dotenv from 'dotenv';
dotenv.config();
const MONGODB_URI = process.env.MONGODB_URI;
async function dbConnect(DB_NAME) {
    try {
        await connect(MONGODB_URI, {
            dbName: DB_NAME,
        });
        console.log(`You successfully connected to ${DB_NAME} MongoDB!`);
    } catch (error) {
        console.log("!!!!!!!!!!!!!!!!!! from mongoose.config.js", error);
        throw error;
    }
}
export default dbConnect;

