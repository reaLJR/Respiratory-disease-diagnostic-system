// import React, { useState, useEffect }  from "react";
// import Tree from "react-d3-tree";

// const DiagnosisTree = () => {
//   // 在这里设置初始的诊断树数据
//   // const initialTreeData = {
//   //   name: "Respiratory diseases",
//   //   children: [
//   //     {
//   //       name: "Upper respiratory tract infections",
//   //       children: [
//   //         { name: "Common cold" },
//   //         { name: "Sinusitis" },
//   //         { name: "Pharyngitis" },
//   //         { name: "Laryngitis" },
//   //       ],
//   //     },
    
//   //   ],
//   // };

//   // const treeData = {
//   //   name: "Diagnosis Tree",
//   //   children: renderTreeNodes(initialTreeData.children),
//   // };

//   const [treeData, setTreeData] = useState();

//   useEffect(() => {
//     fetchData();
//   }, []);

//   const fetchData = async () => {
//     try {
//       const response = await fetch("http://127.0.0.1:8000/tree");
//       const data = await response.json();
//       const updatedTreeData = data.map((disease) => {
//         const { name, treeNode } = disease;
//         const formattedTreeNode = formatTreeNode(treeNode); // 格式化treeNode
//         const renderedTreeNode = renderTreeNodes(formattedTreeNode); // 渲染树节点
//         return {
//           name: name,
//           // children: formattedTreeNode.children,
//           children: renderedTreeNode,

//         };
//       });
//       setTreeData(updatedTreeData);
//     } catch (error) {
//       console.log("Error fetching data:", error);
//     }
//   };

//   const formatTreeNode = (treeNode) => {
//     const { children } = treeNode;
//     if (children && children.length > 0) {
//       const formattedChildren = children.map((child) => formatTreeNode(child));
//       return { children: formattedChildren };
//     }
//     return { children: [] };
//   };

//   // 在这里定义 renderTreeNodes 函数，用于递归渲染诊断树的节点
//   const renderTreeNodes = (nodes) => {
//     return nodes.map((node) => {
//       if (node.children) {
//         return {
//           name: node.name,
//           children: renderTreeNodes(node.children),
//         };
//       }
//       return { name: node.name, className: node.name === "Common cold" ? "path_node" : "" };
//     });
//   };

  

//   return (
//     <div>
//       <h2>Possible Diseases:</h2>

//       <div id="treeWrapper" style={{ width: "50em", height: "20em" }}>
//         <Tree
//           data={treeData}
//           nodeSvgShape={{ shape: "circle", shapeProps: { r: 10 } }}
//         />
//       </div>
//     </div>
//   );
// };

// export default DiagnosisTree;


// import React, { useState, useEffect } from "react";
// import Tree from "react-d3-tree";

// const DiagnosisTree = () => {
//   const [treeData, setTreeData] = useState();

//   useEffect(() => {
//     fetchData();
//   }, []);

//   // const fetchData = async () => {
//   //   try {
//   //     const response = await fetch("http://127.0.0.1:8000/tree");
//   //     const data = await response.json();
//   //     const updatedTreeData = data.map((disease) => {
//   //       const { name, treeNode } = disease;
//   //       const formattedTreeNode = formatTreeNode(treeNode);
//   //       return {
//   //         name: name,
//   //         children: [formattedTreeNode],
//   //       };
//   //     });
//   //     setTreeData(updatedTreeData);
//   //   } catch (error) {
//   //     console.log("Error fetching data:", error);
//   //   }
//   // };

//   const fetchData = async () => {
//     try {
//       const response = await fetch("http://127.0.0.1:8000/tree");
//       const data = await response.json();
//       const updatedTreeData = data.map((disease) => {
//         const { name, treeNode } = disease;
//         const formattedTreeNode = formatTreeNode(treeNode);
//         return {
//           name: name,
//           children: [formattedTreeNode],
//         };
//       });
//       setTreeData(updatedTreeData);
//     } catch (error) {
//       console.log("Error fetching data:", error);
//     }
//   };
  

//   const formatTreeNode = (treeNode) => {
//     const { children } = treeNode;
//     if (children && children.length > 0) {
//       const formattedChildren = children.map((child) => formatTreeNode(child));
//       return {
//         name: treeNode.name,
//         children: formattedChildren,
//       };
//     }
//     return {
//       name: treeNode.name,
//     };
//   };

//   return (
//     <div>
//       <h2>Possible Diseases:</h2>
//       <div id="treeWrapper" style={{ width: "50em", height: "20em" }}>
//         {treeData && (
//           <Tree
//             data={treeData}
//             nodeSvgShape={{ shape: "circle", shapeProps: { r: 10 } }}
//           />
//         )}
//       </div>
//     </div>
//   );
// };

// export default DiagnosisTree;


import React, { useState, useEffect } from "react";
import Tree from "react-d3-tree";

const DiagnosisTree = () => {
  const [treeData, setTreeData] = useState();

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/tree");
      const data = await response.json();
      const updatedTreeData = data.map((disease) => {
        const { name, treeNode } = disease;
        const formattedTreeNode = formatTreeNode(treeNode);
        return {
          name: name,
          children: [formattedTreeNode],
        };
      });
      setTreeData(updatedTreeData);
    } catch (error) {
      console.log("Error fetching data:", error);
    }
  };

  const formatTreeNode = (treeNode) => {
    const { children } = treeNode;
    if (children && children.length > 0) {
      const formattedChildren = children.map((child) => formatTreeNode(child));
      return {
        name: treeNode.name,
        children: formattedChildren,
      };
    }
    return {
      name: treeNode.name,
      children: [],
    };
  };

  return (
    <div>
      <h2>Possible Diseases:</h2>
      <div id="treeWrapper" style={{ width: "50em", height: "20em" }}>
        {treeData && (
          <Tree
            data={treeData}
            nodeSvgShape={{ shape: "circle", shapeProps: { r: 10 } }}
          />
        )}
      </div>
    </div>
  );
};

export default DiagnosisTree;
