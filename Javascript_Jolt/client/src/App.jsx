import "./App.css";
import 'bootstrap/dist/css/bootstrap.min.css';
import { Routes, Route, Navigate } from "react-router-dom";

// components
import Navigation from "./components/Navigation";

// views
import Home from "./views/Home";
import ViewOne from "./views/ViewOne";
import New from "./views/New";
import Edit from "./views/Edit";

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
					<Route path="/coffee/:id" element={ <ViewOne /> } />
					<Route path="/coffee/new" element={ <New /> } />
					<Route path="/coffee/edit/:id" element={ <Edit /> } />
				</Routes>
		</>
	);
}

export default App;
