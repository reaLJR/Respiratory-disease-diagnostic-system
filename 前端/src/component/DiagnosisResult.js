import React from 'react';
import Modal from 'react-modal';
import PossibleDiseases from './PossibleDiseases';
import DiagnosisTree from './DiagnosisTree';

function DiagosisResult({ isOpen, onRequestClose }) {
  const [disease, setDisease] = React.useState('Possible Diseases');

  const handlePossibleDiseasesClick = () => {
    setDisease('Possible Diseases');
  };

  const handleDiagnosisTreeClick = () => {
    setDisease('Diagnosis Tree');
  };

  return (
    
    
    <React.StrictMode>
      


      <div id="blog">
        <div className="blog-content">
          <div className="blog-grid">
            <div class="container">
              <div class="row">
                <div class="col-md-12">
                  <div
                    class="main-title text-center wow fadeIn"
                    style={{ marginTop: "300px" }}
                  >
                    <h3>Please Enter Your Symptoms</h3>

                    <Modal isOpen={isOpen} onRequestClose={onRequestClose}>
                      <h2>Choose an action:</h2>
                      <button onClick={handlePossibleDiseasesClick}>Show Possible Diseases</button>
                      <button onClick={handleDiagnosisTreeClick}>Show Diagnosis Tree</button>
                      {disease === 'Possible Diseases' && <PossibleDiseases />}
                      {disease === 'Diagnosis Tree' && <DiagnosisTree />}
                      <button onClick={onRequestClose}>Close Modal</button>
                    </Modal>


                  </div>
                </div>
              </div>
            </div>
            
          </div>
        </div>
      </div>
    </React.StrictMode>


    
  );
}

export default DiagosisResult;