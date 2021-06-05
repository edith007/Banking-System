import "bootstrap/dist/css/bootstrap.min.css";
import Landing from "./layouts/landing";
import zerver from "./layouts/zerver";
import { Switch, Route } from "react-router-dom";
import "./App.css"

function App() {
  return (
    <div className="App">
      <Switch>
        <Route exact path="/" component={Landing} />
        <Route path="/banks/:ifsc" component={zerver} />
      </Switch>
    </div>
  );
}

export default App;
