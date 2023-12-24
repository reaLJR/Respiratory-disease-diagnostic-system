
import React, { useState, useEffect } from "react";
import { makeStyles } from "@material-ui/core/styles";
import { List, ListItem, ListItemText } from "@material-ui/core";

const useStyles = makeStyles((theme) => ({
  root: {
    width: "100%",
    maxWidth: 360,
    backgroundColor: theme.palette.background.paper,
  },
}));

const tableStyle = {
  borderCollapse: 'collapse',
  width: '100%',
  border: '1px solid #ccc',
  fontFamily: '楷体, KaiTi, Arial, sans-serif',
  color: '#333',
  backgroundColor: '#f2f2f2',
};

const listItemStyle = {
  marginBottom: '10px',
  fontSize: '18px',
  fontWeight: 'bold',
  fontFamily: 'Arial, sans-serif',
  color: '#333',
};


const PossibleDiseases = () => {
    const [diseases, setDiseases] = useState([]);
  
    useEffect(() => {
      fetch("http://127.0.0.1:8000/diseases")
        .then((response) => response.json())
        .then((data) => setDiseases(data))
        .catch((error) => console.error(error));
    }, []);
  
    console.log(diseases);

    return (
      // <div>
      //   <h2>Possible Diseases:</h2>
      //   <List className={classes.root}>
      //   {/* 使用map()方法来生成多个列表项 */}
      //   {diseaseNames.map((name) => (
      //     <ListItem key={name}>
      //       <ListItemText primary={name} />
      //     </ListItem>
      //   ))}
      // </List>
      //   <ul>
      //     {diseases.map((disease) => (
      //       <li key={diseaseName}>{diseaseName ? disease.name : 'healthy'}</li>
      //     ))}
      //   </ul>
      // </div>
      <div>
        <h2>Possible Diseases:</h2>
        <ul>
          {diseases.map((disease, index) => (
            <ul>
            {diseases.map((disease, index) => (
              <li key={index} style={listItemStyle}>
                {disease.name}
                <table style={tableStyle}>
                  <tbody>
                    <tr>
                      <td>中文名称</td>
                      <td>{disease.chinese_name}</td>
                    </tr>
                    <tr>
                      <td>链接</td>
                      <td>{disease.link}</td>
                    </tr>
                    <tr>
                      <td>路径介绍</td>
                      <td>{disease.path}</td>
                    </tr>
                  </tbody>
                </table>
              </li>
            ))}
          </ul>
          
            // <li key={index}>{disease.name}</li>
          ))}
        </ul>
      </div>
    );
  };
  

export default PossibleDiseases;

// import React, { useState, useEffect } from "react";
// import { makeStyles } from "@material-ui/core/styles";
// import { List, ListItem, ListItemText } from "@material-ui/core";

// const useStyles = makeStyles((theme) => ({
//   root: {
//     width: "100%",
//     maxWidth: 360,
//     backgroundColor: theme.palette.background.paper,
//   },
// }));

// const PossibleDiseases = () => {
//   const [diseases, setDiseases] = useState([]);

//   useEffect(() => {
//     fetch("http://127.0.0.1:5000/diseases")
//       .then((response) => response.json())
//       .then((data) => setDiseases(data))
//       .catch((error) => console.error(error));
//   }, []);

//   console.log(diseases);

//   // 假设需要展示的疾病名称存储在一个数组中
//   const diseaseNames = ["支气管肺炎"];

//   const classes = useStyles();

//   return (
//     <div>
//       <h2>Possible Diseases:</h2>
//       <List className={classes.root}>
//         {/* 使用map()方法来生成多个列表项 */}
//         {diseaseNames.map((name) => (
//           <ListItem key={name}>
//             <ListItemText primary={name} />
//           </ListItem>
//         ))}
//       </List>
//     </div>
//   );
// };

// export default PossibleDiseases;

