import React, { useState, useEffect } from "react";
import { useHistory } from "react-router-dom";
import Modal from 'react-modal';
import PossibleDiseases from '../component/PossibleDiseases';
import DiagnosisTree from '../component/DiagnosisTree';
import DiagnosisResult from "../component/DiagnosisResult";
import SyntaxHighlighter from "react-syntax-highlighter";
import { docco } from "react-syntax-highlighter/dist/esm/styles/hljs";

const FormExample = () => {
  const id = -1; // 假设 id 变量的默认值为 -1
  const data = { id: id }; // 将 id 变量添加到请求主体中
  
  const [name, setName] = useState("");
  const [age, setAge] = useState("");
  const [gender, setGender] = useState("");
  const [disease, setDisease] = useState("");
  const [selectedSymptoms, setSelectedSymptoms] = useState([]);
  const [symptomType, setSymptomType] = useState("");
  const [symptomName, setSymptomName] = useState("");

  // const symptomTypes = [    "Coughing",    "Sneezing",    "Fever",    "Headache",    "Fatigue",    "Nausea",    "Dizziness",    "Chest Pain",    "Abdominal Pain",    "Other"  ];

  // const symptomsList = {
  //   Coughing: [
  //     "Dry cough",
  //     "Productive cough",
  //     "Blood in cough",
  //     "Chest pain during cough"
  //   ],
  //   Sneezing: [
  //     "Frequent sneezing",
  //     "Runny nose",
  //     "Nasal congestion"
  //   ],
  //   Fever: [
  //     "High fever",
  //     "Low fever",
  //     "Feverish chills"
  //   ],
  //   Headache: [
  //     "Migraine",
  //     "Tension headache",
  //     "Sinus headache"
  //   ],
  //   Fatigue: [
  //     "General fatigue",
  //     "Muscle weakness",
  //     "Mental fatigue"
  //   ],
  //   Nausea: [
  //     "Feeling sick",
  //     "Vomiting",
  //     "Loss of appetite"
  //   ],
  //   Dizziness: [
  //     "Vertigo",
  //     "Lightheadedness",
  //     "Fainting"
  //   ],
  //   "Chest Pain": [
  //     "Sharp chest pain",
  //     "Dull chest pain",
  //     "Pressure in chest"
  //   ],
  //   "Abdominal Pain": [
  //     "Upper abdominal pain",
  //     "Lower abdominal pain",
  //     "Bloating"
  //   ],
  //   Other: [
  //     "Other symptoms",
  //     'sore_throat', 
  //     'fever', 
  //     'cough'
  //   ]
  // };

  const [symptomTypes, setSymptomTypes] = useState([]);
  const [symptomsList, setSymptomsList] = useState({});

  useEffect(() => {
    // 在组件加载时获取数据
    fetch('http://127.0.0.1:8000/symptoms')
      .then(response => response.json())
      .then(data => {
        // 从获取的数据中提取症状类型和症状列表
        const { symptomTypes, symptomsList } = data;

        // 更新组件的状态或变量
        setSymptomTypes(symptomTypes);
        setSymptomsList(symptomsList);
      })
      .catch(error => {
        console.error('Error fetching symptom data:', error);
      });
  }, []);

  const handleSymptomTypeChange = (event) => {
    setSymptomType(event.target.value);
    setSymptomName("");
  };

  const handleSymptomNameChange = (event) => {
    setSymptomName(event.target.value);
  };

  const handleAddSymptom = (event) => {
    event.preventDefault();
    if (symptomName) {
      setSelectedSymptoms([...selectedSymptoms, symptomName]);
      setSymptomName("");
    }
  };

  const handleRemoveSymptom = (symptom) => {
    setSelectedSymptoms(selectedSymptoms.filter((s) => s !== symptom));
  };
  // const history = useHistory(); // 初始化useHistory hook

  const handleSubmit = (event) => {
    event.preventDefault();
    const formData = new FormData();
    formData.append('name', name);
    formData.append('age', age);
    formData.append('gender', gender);
    formData.append('disease', disease);
    formData.append('symptoms', selectedSymptoms.join(","));
    fetch('http://127.0.0.1:8000/submit_patient_form', {
        method: 'POST',
        body: formData,
    }).then(response => {
        if (response.ok) {
        console.log('Form data submitted successfully');
        setShowModal(true); // 表单提交成功后显示弹窗
        // 表单提交成功后自动跳转到PossibleDiseases组件所在路由
        // history.push('/diagnosis-result');
        } else {
        console.log('Form data submission failed');
        }
    }).catch(error => {
        console.error('Form data submission failed:', error);
    });
  };

  fetch('http://127.0.0.1:8000/disease_id', {
    method: 'POST', // 或其他 HTTP 方法
    body: JSON.stringify(data), // 将数据转换为字符串并添加到请求主体中
    headers: {
      'Content-Type': 'application/json' // 指定请求主体的数据类型
    }
    // 其他 fetch 选项
  }).then(response => {
    // 处理响应
  }).catch(error => {
    // 处理错误
  });

  // Popup window function
  const [showModal, setShowModal] = useState(false);

  useEffect(() => {
    setDisease('Possible Diseases');
  }, []); // 在组件挂载时设置默认值

  const handleModalClose = () => {
    setShowModal(false);
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
                    style={{ marginTop: "80px" }}
                  >
                    <h3>Please Enter Your Symptoms</h3>

                    <div className="patient-form">
                    <div className="banner">
                      <form onSubmit={handleSubmit}>
                        <div>
                          <label>
                            Name:
                            <input type="text" value={name} onChange={(e) => setName(e.target.value)} />
                          </label>
                        </div>
                        <div>
                          <label>
                            Age:
                            <input type="text" value={age} onChange={(e) => setAge(e.target.value)} />
                          </label>
                        </div>
                        <div>
                          <label>
                            Gender:
                            <select value={gender} onChange={(e) => setGender(e.target.value)}>
                              <option value="">Select Gender</option>
                              <option value="male">Male</option>
                              <option value="female">Female</option>
                            </select>
                          </label>
                        </div>
                        <div>
                          <label>
                            Symptoms:
                            <select value={symptomType} onChange={handleSymptomTypeChange}>
                              <option value="">Select symptom type</option>
                              {symptomTypes.map((type) => (
                                <option key={type} value={type}>
                                  {type}
                                </option>
                              ))}
                            </select>
                            {symptomType && (
                              <select value={symptomName} onChange={handleSymptomNameChange}>
                                <option value="">Select symptom name</option>
                                {symptomsList[symptomType].map((symptom) => (
                                  <option key={symptom} value={symptom}>
                                    {symptom}
                                  </option>
                                ))}
                              </select>
                            )}
                            <button onClick={handleAddSymptom}>Add</button>
                          </label>
                        </div>
                        <div>
                          <ul>
                            {selectedSymptoms.map((symptom) => (
                              <li key={symptom}>
                                {symptom}
                                <button type="button" onClick={() => handleRemoveSymptom(symptom)}>Remove</button>
                              </li>
                            ))}
                          </ul>
                        </div>
                        
                        <button type="submit">Submit</button>    
                              
                        <DiagnosisResult isOpen={showModal} onRequestClose={handleModalClose} />
                      </form>
                    </div>
                  </div>


                    
                  </div>
                </div>
              </div>
            </div>
           
          </div>
        </div>
      </div>
    </React.StrictMode>
  );
};

export default FormExample;
