import React, { useState, useEffect } from 'react';
import { Table } from 'antd';
import { Modal } from 'antd';
import DiagnosisResult from "../component/DiagnosisResult";



const columns = [
  {
    title: '病历号',
    dataIndex: 'id',
    key: 'id',
  },
  {
    title: '姓名',
    dataIndex: 'name',
    key: 'name',
  },
  {
    title: '诊断时间',
    dataIndex: 'diagnosisTime',
    key: 'diagnosisTime',
  },
  {
    title: '诊断结果',
    dataIndex: 'diagnosisResult',
    key: 'diagnosisResult',
  },
];

// const data = [
//   {
//     key: '1',
//     id: '1',
//     name: '张三',
//     diagnosisTime: '2021-01-01',
//     diagnosisResult: '感冒',
//   },
//   {
//     key: '2',
//     id: '2',
//     name: '李四',
//     diagnosisTime: '2021-01-02',
//     diagnosisResult: '发烧',
//   },
//   {
//     key: '3',
//     id: '3',
//     name: '王五',
//     diagnosisTime: '2021-01-03',
//     diagnosisResult: '感冒',
//   },
//   {
//     key: '4',
//     id: '4',
//     name: '赵六',
//     diagnosisTime: '2021-01-04',
//     diagnosisResult: '感冒',
//   },
//   {
//     key: '5',
//     id: '5',
//     name: '钱七',
//     diagnosisTime: '2021-01-05',
//     diagnosisResult: '发烧',
//   },
//   {
//     key: '6',
//     id: '6',
//     name: '孙八',
//     diagnosisTime: '2021-01-06',
//     diagnosisResult: '感冒',
//   },
//   {
//     key: '7',
//     id: '7',
//     name: '周九',
//     diagnosisTime: '2021-01-07',
//     diagnosisResult: '感冒',
//   },
//   {
//     key: '8',
//     id: '8',
//     name: '吴十',
//     diagnosisTime: '2021-01-08',
//     diagnosisResult: '发烧',
//   },
//   {
//     key: '9',
//     id: '9',
//     name: '郑十一',
//     diagnosisTime: '2021-01-09',
//     diagnosisResult: '感冒',
//   },
// ];

// const data = [
//   {
//     key: '1',
//     id: '1',
//     name: 'Alice',
//     diagnosisTime: '2023-04-01',
//     diagnosisResult: '支气管肺炎',
//   },
//   {
//     key: '2',
//     id: '2',
//     name: 'Alice',
//     diagnosisTime: '2023-04-01',
//     diagnosisResult: '急性呼吸道感染',
//   },
//   {
//     key: '3',
//     id: '3',
//     name: 'Alice',
//     diagnosisTime: '2023-04-01',
//     diagnosisResult: '中枢型呼吸衰竭',
//   },
//   {
//     key: '4',
//     id: '4',
//     name: 'Alice',
//     diagnosisTime: '2023-04-01',
//     diagnosisResult: '慢性阻塞性肺疾病',
//   },
//   {
//     key: '5',
//     id: '5',
//     name: 'Alice',
//     diagnosisTime: '2023-04-01',
//     diagnosisResult: '气胸',
//   },
//   {
//     key: '6',
//     id: '6',
//     name: 'Alice',
//     diagnosisTime: '2023-04-01',
//     diagnosisResult: '肺不张',
//   },
//   {
//     key: '7',
//     id: '7',
//     name: 'Alice',
//     diagnosisTime: '2023-04-01',
//     diagnosisResult: '哮喘',
//   },
//   {
//     key: '8',
//     id: '8',
//     name: 'Alice',
//     diagnosisTime: '2023-04-01',
//     diagnosisResult: '间质性肺疾病',
//   },
//   {
//     key: '9',
//     id: '9',
//     name: 'Alice',
//     diagnosisTime: '2023-04-01',
//     diagnosisResult: '肺结核',
//   },
// ];

  




const UiUx = () => {
  const [isDiagnosisResultOpen, setIsDiagnosisResultOpen] = useState(false);
  const [data, setData] = useState([]);
  const [selectedRecord, setSelectedRecord] = useState(null);


  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/history');
        const jsonData = await response.json();
        setData(jsonData);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  const handleRowClick = (record, rowIndex) => {
    // setIsDiagnosisResultOpen(true);
    setSelectedRecord(record);
    setIsDiagnosisResultOpen(true);
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
                    <h3>History Records</h3>


                    <Table
                      columns={columns}
                      dataSource={data}
                      onRow={(record, rowIndex) => ({
                        onClick: () => handleRowClick(record, rowIndex)
                      })} />


                      <Modal
                            visible={isDiagnosisResultOpen}
                            onCancel={() => setIsDiagnosisResultOpen(false)}
                          >
                            {selectedRecord && (
                              <>
                                <p>Mr_Id: {selectedRecord.id}</p>
                                <p>Name: {selectedRecord.name}</p>
                                <p>Time: {selectedRecord.diagnosisTime}</p>
                                <p>Possible Diseases:</p>
                                <ul>
                                  {selectedRecord.diagnosisResult.map((disease) => (
                                    <li key={disease}>{disease}</li>
                                  ))}
                                </ul>
                              </>
                            )}
                          </Modal>

                    {/* <DiagnosisResult isOpen={isDiagnosisResultOpen} onRequestClose={() => setIsDiagnosisResultOpen(false)} /> */}



                    <div class="underline1"></div>
                    <div class="underline2"></div>
                    
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

export default UiUx;
