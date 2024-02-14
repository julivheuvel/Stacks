import "./App.css";
import { Routes, Route, Navigate } from "react-router-dom";

import Navigation from "./components/Navigation";
import Home from "./views/Home";

function App() {
	return (
		<>
			{/* not inside of a route and therefore in components folder */}
			<Navigation />

				<Routes>
					{/* navigate => redirect */}
					<Route path="/" element={ <Navigate to="/coffee" /> } />
					{/* inside of a route and therefore in views folder */}
					<Route path="/coffee" element={ <Home /> } />
				</Routes>
		</>
	);
}

export default App;
