import './App.css';
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Navbar from "./components/Navbar"
import Editor from "./pages/Editor"
import Test from "./pages/Test"
// import Sheeps from "./pages/Sheeps"
// import Goats from "./pages/Goats"
function App() {
  return (
    <Router>
      <Navbar />
      <Switch>
        <Route path='/' exact component={Editor} />
        <Route path='/Test' component={Test} />
        {/* <Route path='/sheeps' component={Sheeps} />
        <Route path='/goats' component={Goats} /> */}
      </Switch>
    </Router>
  );
}

export default App;