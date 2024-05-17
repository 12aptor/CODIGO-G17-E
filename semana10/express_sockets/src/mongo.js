import { MongoClient } from "mongodb";

const uri = "mongodb://localhost:27017";
const mongoClient = new MongoClient(uri);
const conn = await mongoClient.connect();
export const testDb = conn.db("test");
