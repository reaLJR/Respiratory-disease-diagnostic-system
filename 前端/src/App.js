import React from "react";
import "./App.css";

// import Router
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

// import Component
import Header from "./component/Header";
import Footer from "./component/Footer";
import ScrollToTop from "./component/ScrollToTop";

// import Pages
import Home from "./Pages/Home";
import ReactHooks from "./Pages/ReactHooks";
import UiUx from "./Pages/UiUx";
import FormExample from "./Pages/FormExample";

import PossibleDiseases from './component/PossibleDiseases';
import DiagnosisTree from './component/DiagnosisTree';
import Welcome from './component/Welcome';
import Sidebar from './component/SideBar';
import DiagnosisResult from './component/DiagnosisResult';

import HistoryRecord from './Pages/HistoryRecord';
import PatientForm from './Pages/PatientForm';
import EditKnowledge from './Pages/EditKnowledge';

function App() {
  return (
    <React.StrictMode>
      <Router>
        <Header />
        <ScrollToTop>
          <Switch>
            <Route exact path="/" component={Home} />
            <Route exact path="/react-hooks" component={ReactHooks} />
            <Route exact path="/ui-ux" component={UiUx} />
            <Route exact path="/form-example" component={FormExample} />

            <Route path="/patient-form" element={<PatientForm />} />
            <Route path="/possible-diseases" element={<PossibleDiseases />} />
            <Route path="/diagnosis-tree" element={<DiagnosisTree />} />
            <Route path="/diagnosis-result" element={<DiagnosisResult />} />
            <Route path="/welcome" element={<Welcome />} />
            <Route path="/history-record" element={<HistoryRecord />} />
            <Route path="/edit-knowledge" element={<EditKnowledge />} />
          </Switch>
        </ScrollToTop>
        <Footer />
      </Router>
    </React.StrictMode>
  );
}

export default App;
