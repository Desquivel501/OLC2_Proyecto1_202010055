import 'react-bootstrap-table-next/dist/react-bootstrap-table2.min.css';
import BootstrapTable from "react-bootstrap-table-next";
import React, { Component } from "react";

const columns = [
    {
      dataField: "userId",
      text: "id",
    },
    {
      dataField: "title",
      text: "title"
    },
     {
      dataField: "completed",
      text: "completed"
    },
  ];

export const TablaSimbolos = ({data}) => {
    return (
        <div className='col d-flex flex-column justify-content-evenly'>
            
        </div>
    )
}





// const columns = [
//     {
//       dataField: "userId",
//       text: "id",
//     },
//     {
//       dataField: "title",
//       text: "title"
//     },
//      {
//       dataField: "completed",
//       text: "completed"
//     },
//   ];

//   const url = 'https://jsonplaceholder.typicode.com/todos/'


//   class TablaSimbolos extends React.Component {
//     state = { data: null };

//     async componentDidMount() {
//       const { data } = await axios.get(url)

//       this.setState({ data });
//     }

//     render() {
//       if (!this.state.data) return null;
//       console.log(this.state.data);

//       return (
//         <BootstrapTable
//           keyField="id"
//           data={this.state.data}
//           columns={columns}
//           striped
//           hover
//           condensed
//           // pagination={paginationFactory({})}
//         />
//       )
//     }
//   }

