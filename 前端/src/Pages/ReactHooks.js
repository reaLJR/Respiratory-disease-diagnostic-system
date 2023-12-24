import React, { useState, useEffect } from 'react';
import SyntaxHighlighter from "react-syntax-highlighter";
import { docco } from "react-syntax-highlighter/dist/esm/styles/hljs";

const ReactHooks = () => {
  const [diagnosisNode, setDiagnosisNode] = useState('');
  const [diagnosisPath, setDiagnosisPath] = useState('');
  const [deleteNode, setDeleteNode] = useState('');
  const [deletePath, setDeletePath] = useState('');
  const [successMessage, setSuccessMessage] = useState('');

  const [symptomType, setSymptomType] = useState("");
  const [symptomName, setSymptomName] = useState("");
  const [symptomTypes, setSymptomTypes] = useState([]);
  const [symptomsList, setSymptomsList] = useState({});

  const [inputValue, setInputValue] = useState('');

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

  const handleSubmit = async (event, url) => {
    event.preventDefault();
    
    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          diagnosisNode,
          diagnosisPath,
          deleteNode,
          deletePath
        })
      });
      
      if (response.ok) {
        setSuccessMessage('操作成功');
      } else {
        setSuccessMessage('操作失败');
      }
    } catch (error) {
      console.error('Error submitting data:', error);
    }
  };

  const handleSymptomTypeChange = (event) => {
    setSymptomType(event.target.value);
    setSymptomName("");
  };

  const handleSymptomNameChange = (event) => {
    setSymptomName(event.target.value);
  };

  const handleAction = (actionType) => {
    if (actionType === "Delete") {
      // 执行删除操作
      if (symptomName) {
        // 发送请求到后端，将删除的 symptomName 数据发送到 http://127.0.0.1:8000/edit
        fetch("http://127.0.0.1:8000/edit", {
          method: "POST",
          body: JSON.stringify({
            type: "delete",
            delete: symptomName,
            label: "symptom",
          }),
          headers: {
            "Content-Type": "application/json",
          },
        })
          .then((response) => response.json())
          .then((data) => {
            // 处理响应结果
            console.log(data);
          })
          .catch((error) => {
            console.error("Error deleting symptom:", error);
          });
      }
    } else if (actionType === "Edit") {
      if (symptomName && inputValue) {
        // 发送请求到后端，将删除的 symptomName 数据发送到 http://127.0.0.1:8000/edit
        fetch("http://127.0.0.1:8000/edit", {
          method: "POST",
          body: JSON.stringify({
            type: "edit",
            edit_from: symptomName,
            edit_to:inputValue,
            label: "symptom",
          }),
          headers: {
            "Content-Type": "application/json",
          },
        })
          .then((response) => response.json())
          .then((data) => {
            // 处理响应结果
            console.log(data);
          })
          .catch((error) => {
            console.error("Error deleting symptom:", error);
          });
      }// 执行编辑操作
      // ...
    } else if (actionType === "Add") {
      // 执行添加操作
      if (inputValue) {
        // 发送请求到后端，将添加的 inputValue 数据发送到 http://127.0.0.1:8000/edit
        fetch("http://127.0.0.1:8000/edit", {
          method: "POST",
          body: JSON.stringify({
            type: "add",
            add: inputValue,
            label: "symptom",
          }),
          headers: {
            "Content-Type": "application/json",
          },
        })
          .then((response) => response.json())
          .then((data) => {
            // 处理响应结果
            console.log(data);
          })
          .catch((error) => {
            console.error("Error adding symptom:", error);
          });
      }
    }
  };

  const handleInputChange = (event) => {
    const value = event.target.value;
    setInputValue(value);
  };



  const [selectedValue, setSelectedValue] = useState("");
  const [leftInput, setLeftInput] = useState("");
  const [rightInput, setRightInput] = useState("");

  const handleSelectedValueChange = (event) => {
    setSelectedValue(event.target.value);
  };

  const handleLeftInputChange = (event) => {
    setLeftInput(event.target.value);
  };

  const handleRightInputChange = (event) => {
    setRightInput(event.target.value);
  };

  const handleReplaceButtonClick = () => {
    // 构建请求数据
    const requestData = {
      type: "edit",
      edit_from: leftInput,
      edit_to: rightInput,
      label: selectedValue,
    };

    // 发送POST请求
    fetch("http://127.0.0.1:8000/edit", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(requestData),
    })
      .then((response) => response.json())
      .then((data) => {
        // 处理响应数据
        console.log(data);
      })
      .catch((error) => {
        console.log("Error:", error);
      });
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
                    <h3>修改诊断路径</h3>
                    <div class="underline1"></div>
                    <div class="underline2"></div>
                    <p>
                      Enter your changes please.
                    </p>
                  </div>
                </div>
              </div>
            </div>



            <div className="blog-details wow fadeIn text-left">
              <div className="container">
                <div
                  className="row"
                  style={{
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <div className="col-xl-9 col-lg-9 col-md-12 col-xs-12 col-sm-12">
                    <div className="blog-main">

                    

                        {/* <div>
                          <form onSubmit={(event) => handleSubmit(event, 'http://127.0.0.1:8000/edit')}>
                            <label>
                              Add Diagnosis Node:
                              <input
                                type="text"
                                value={diagnosisNode}
                                onChange={(event) => setDiagnosisNode(event.target.value)}
                              />
                            </label>
                            <button type="submit">Submit</button>
                          </form>

                          <form onSubmit={(event) => handleSubmit(event, 'http://127.0.0.1:8000/edit')}>
                            <label>
                              Add Diagnosis Path:
                              <input
                                type="text"
                                value={diagnosisPath}
                                onChange={(event) => setDiagnosisPath(event.target.value)}
                              />
                            </label>
                            <button type="submit">Submit</button>
                          </form>

                          <form onSubmit={(event) => handleSubmit(event, 'http://127.0.0.1:8000/edit')}>
                            <label>
                              Delete Diagnosis Node:
                              <input
                                type="text"
                                value={deleteNode}
                                onChange={(event) => setDeleteNode(event.target.value)}
                              />
                            </label>
                            <button type="submit">Submit</button>
                          </form>

                          <form onSubmit={(event) => handleSubmit(event, 'http://127.0.0.1:8000/edit')}>
                            <label>
                              Delete Diagnosis Path:
                              <input
                                type="text"
                                value={deletePath}
                                onChange={(event) => setDeletePath(event.target.value)}
                              />
                            </label>
                            <button type="submit">Submit</button>
                          </form>

                          {successMessage && <div>{successMessage}</div>}
                        </div> */}

                        <div>
                        <div class="underline1"></div>
                    <div class="underline2"></div>

                          <h2>Edit Symptoms</h2>
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
                            <div>
                              <input type="text" value={inputValue} onChange={handleInputChange} />
                              <button onClick={() => handleAction("Delete")}>Delete</button>
                              <button onClick={() => handleAction("Edit")}>Edit</button>
                              <button onClick={() => handleAction("Add")}>Add</button>
                            </div>

                            <p>Rules: 填写文本框添加结点，选择症状删除该结点，选择症状修改其为文本框内容</p>

                            


                            {/* <button onClick={handleAddSymptom}>Add</button> */}
                          </label>
                        </div>
                      
                    </div>
                    
                  </div>
                </div>
              </div>
            </div>

            <div className="blog-details wow fadeIn text-left">
              <div className="container">
                
                <div
                  className="row"
                  style={{
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <div className="col-xl-9 col-lg-9 col-md-12 col-xs-12 col-sm-12">
                    <div className="blog-main">

                    <div>
                    <div class="underline1"></div>
                    <div class="underline2"></div>

                        <h2>Edit Nodes</h2>
                        <label>
                          Select Value:
                          <select value={selectedValue} onChange={handleSelectedValueChange}>
                            <option value="disease">Disease</option>
                            <option value="item">Item</option>
                          </select>
                        </label>
                        <br />
                        <label>
                          Change:
                          <input type="text" value={leftInput} onChange={handleLeftInputChange} />
                        </label>
                        <br />
                        <label>
                          To:
                          <input type="text" value={rightInput} onChange={handleRightInputChange} />
                        </label>
                        <br />
                        <button onClick={handleReplaceButtonClick}>Replace</button>
                        <p>Rules: 仅填写 Change 框则添加结点，仅填写 To 则删除该结点，都填写则改变 Change 结点为 To 结点的属性</p>
                      </div>

                        {/* <div>
                          <form onSubmit={(event) => handleSubmit(event, 'http://127.0.0.1:8000/edit')}>
                            <label>
                              Add Diagnosis Node:
                              <input
                                type="text"
                                value={diagnosisNode}
                                onChange={(event) => setDiagnosisNode(event.target.value)}
                              />
                            </label>
                            <button type="submit">Submit</button>
                          </form>

                          <form onSubmit={(event) => handleSubmit(event, 'http://127.0.0.1:8000/edit')}>
                            <label>
                              Add Diagnosis Path:
                              <input
                                type="text"
                                value={diagnosisPath}
                                onChange={(event) => setDiagnosisPath(event.target.value)}
                              />
                            </label>
                            <button type="submit">Submit</button>
                          </form>

                          <form onSubmit={(event) => handleSubmit(event, 'http://127.0.0.1:8000/edit')}>
                            <label>
                              Delete Diagnosis Node:
                              <input
                                type="text"
                                value={deleteNode}
                                onChange={(event) => setDeleteNode(event.target.value)}
                              />
                            </label>
                            <button type="submit">Submit</button>
                          </form>

                          <form onSubmit={(event) => handleSubmit(event, 'http://127.0.0.1:8000/edit')}>
                            <label>
                              Delete Diagnosis Path:
                              <input
                                type="text"
                                value={deletePath}
                                onChange={(event) => setDeletePath(event.target.value)}
                              />
                            </label>
                            <button type="submit">Submit</button>
                          </form>

                          {successMessage && <div>{successMessage}</div>}
                        </div> */}

                        <div>
                          <label>
                            

                            {/* <div>
                        <h2>Edit Paths</h2>
                        <label>
                          Select Value:
                          <select value={selectedValue} onChange={handleSelectedValueChange}>
                            <option value="HAS_BRANCH">Relationship Branch</option>
                            <option value="HAS_BRANCH_COMBINATION">Logic Branch</option>
                          </select>
                        </label>
                        <br />
                        <label>
                          Change:
                          <input type="text" value={leftInput} onChange={handleLeftInputChange} />
                        </label>
                        <br />
                        <label>
                          To:
                          <input type="text" value={rightInput} onChange={handleRightInputChange} />
                        </label>
                        <br />
                        <button onClick={handleReplaceButtonClick}>Replace</button>
                        <p>Rules: 输入为(relation_from, relation_to)的形式，用来表示从 relation_from 到 relation_to 的关系，仅填写 Change 框则添加该关系，仅填写 To 则删除该关系，都填写则改变 Change 关系为 To 关系的属性</p>
                      </div> */}


                          </label>
                        </div>
                      
                    </div>
                    
                  </div>
                </div>
              </div>
            </div>

            <div className="blog-details wow fadeIn text-left">
              <div className="container">
                <div
                  className="row"
                  style={{
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <div className="col-xl-9 col-lg-9 col-md-12 col-xs-12 col-sm-12">
                    <div className="blog-main">

                    

                    <div class="underline1"></div>
                    <div class="underline2"></div>

                        <div>
                          <label>
                          
                            <div>
                            

                        <h2>Edit Paths</h2>
                        <label>
                          Select Value:
                          <select value={selectedValue} onChange={handleSelectedValueChange}>
                            <option value="HAS_BRANCH">Relationship Branch</option>
                            <option value="HAS_BRANCH_COMBINATION">Logic Branch</option>
                          </select>
                        </label>
                        <br />
                        <label>
                          Change:
                          <input type="text" value={leftInput} onChange={handleLeftInputChange} />
                        </label>
                        <br />
                        <label>
                          To:
                          <input type="text" value={rightInput} onChange={handleRightInputChange} />
                        </label>
                        <br />
                        <button onClick={handleReplaceButtonClick}>Replace</button>
                        <p>Rules: 输入为(relation_from, relation_to)的形式，用来表示从 relation_from 到 relation_to 的关系，仅填写 Change 框则添加该关系，仅填写 To 则删除该关系，都填写则改变 Change 关系为 To 关系的属性</p>
                      </div>


                            {/* <button onClick={handleAddSymptom}>Add</button> */}
                          </label>
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

export default ReactHooks;
