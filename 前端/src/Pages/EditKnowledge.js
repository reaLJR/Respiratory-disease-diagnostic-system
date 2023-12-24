import React, { useState } from 'react';
import { Button, Modal, Input } from 'antd';

function EditKnowledge() {
  const [visible, setVisible] = useState(false);
  const [modalTitle, setModalTitle] = useState('');
  const [inputValue, setInputValue] = useState('');

  const showModalAdd = () => {
    setModalTitle('添加诊断路径');
    setVisible(true);
    setInputValue('');
  };

  const showModalDelete = () => {
    setModalTitle('删除诊断路径');
    setVisible(true);
  };

  const showModalEdit = () => {
    setModalTitle('修改诊断路径');
    setVisible(true);
  };

  const showModalView = () => {
    setModalTitle('查看疾病知识库');
    setVisible(true);
  };

  const handleOk = () => {
    setVisible(false);
    if (modalTitle === '添加诊断路径') {
      fetch('./add-disease', {
        method: 'POST',
        body: JSON.stringify({ inputValue }),
        headers: {
          'Content-Type': 'application/json'
        }
      })
    }
  };

  const handleCancel = () => {
    setVisible(false);
  };

  return (
    <div>
      <Button onClick={showModalAdd}>添加诊断路径</Button>
      <Button onClick={showModalDelete}>删除诊断路径</Button>
      <Button onClick={showModalEdit}>修改诊断路径</Button>
      <Button onClick={showModalView}>查看疾病知识库</Button>
      <Modal
        title={modalTitle}
        visible={visible}
        onOk={handleOk}
        onCancel={handleCancel}
      >
        {modalTitle === '添加诊断路径' && <Input onChange={(e) => setInputValue(e.target.value)} />}
      </Modal>
    </div>
  );
}

export default EditKnowledge;





