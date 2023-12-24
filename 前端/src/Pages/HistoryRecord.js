import React, { useState, useEffect } from 'react';
import { Table } from 'antd';
import DiagnosisResult from "../component/DiagnosisResult";


const columns = [
  {
    title: 'id',
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

const data = [
  {
    key: '1',
    id: '1',
    name: 'Alice',
    diagnosisTime: '2023-04-01',
    diagnosisResult: '支气管肺炎',
  },
  {
    key: '2',
    id: '2',
    name: 'Alice',
    diagnosisTime: '2023-04-01',
    diagnosisResult: '急性呼吸道感染',
  },
  {
    key: '3',
    id: '3',
    name: 'Alice',
    diagnosisTime: '2023-04-01',
    diagnosisResult: '中枢型呼吸衰竭',
  },
  {
    key: '4',
    id: '4',
    name: 'Alice',
    diagnosisTime: '2023-04-01',
    diagnosisResult: '慢性阻塞性肺疾病',
  },
  {
    key: '5',
    id: '5',
    name: 'Alice',
    diagnosisTime: '2023-04-01',
    diagnosisResult: '气胸',
  },
  {
    key: '6',
    id: '6',
    name: 'Alice',
    diagnosisTime: '2023-04-01',
    diagnosisResult: '肺不张',
  },
  {
    key: '7',
    id: '7',
    name: 'Alice',
    diagnosisTime: '2023-04-01',
    diagnosisResult: '哮喘',
  },
  {
    key: '8',
    id: '8',
    name: 'Alice',
    diagnosisTime: '2023-04-01',
    diagnosisResult: '间质性肺疾病',
  },
  {
    key: '9',
    id: '9',
    name: 'Alice',
    diagnosisTime: '2023-04-01',
    diagnosisResult: '肺结核',
  },
];

function HistoryRecord() {
  const [isDiagnosisResultOpen, setIsDiagnosisResultOpen] = useState(false);

  const handleRowClick = (record, rowIndex) => {
    setIsDiagnosisResultOpen(true);
  };

  return (
    <>

      <Table columns={columns} dataSource={data} onRow={(record, rowIndex) => ({ onClick: () => handleRowClick(record, rowIndex) })} />

      <DiagnosisResult isOpen={isDiagnosisResultOpen} onRequestClose={() => setIsDiagnosisResultOpen(false)} />
    </>
  );
}

export default HistoryRecord;