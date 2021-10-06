// This method is for role identification and have different graphical Interface 
var el_down = document.getElementById("GFG_DOWN");
function GFG_click(clicked) {
  el_down.innerHTML = "You are the "+clicked+".";
  if (clicked=="Head of Department") {
    document.getElementById('text').innerHTML="Please Upload an Excel Folder"
    document.getElementById('text1').innerHTML="Please Choose the Folder"
    document.getElementById('myFile1').style.display="inline-block"
    document.getElementById('myFile').style.display="none"
  }
  else {
    document.getElementById('text').innerHTML="Please Upload Excel File"
    document.getElementById('text1').innerHTML="Please Select the correct file format"
    document.getElementById('myFile').style.display="inline-block"
    document.getElementById('myFile1').style.display="none"
  }
}

// document.getElementById('role1').onclick = function(){
//     this.style.backgroundColor = 'Yellow';
// };

function showAndHide() {
  const x = document.getElementById("radio");
  if (x.style.display == "block") {
    x.style.display = "none";
  } else {
    x.style.display = "block";
  }
}

/**Used to get data from server side 
 * @param does not have parameter 
 * function fetch the data and return a response of an array of data 
 * pass into the window.onload for plot the bar graph
*/

// get the data from database 
const getAllData = () => {
  fetch('http://127.0.0.1:5000/get_all_data', {
    method:"GET",
    headers:{
      headers: {
        "Content-Type":"application/json"
      }
    }
  })
  .then(resp => resp.json())
  .then((data) => 
    window.onload(data))
  .catch(error => 
    console.log(error))
}

/**Plot a bar graph 
 * @param data type=array, receive data from server 
 * plot the data dynamically based on data from database 
*/

// drawing a bar chart 
window.onload = function (data) {
  const dataArray = []
  for(var i = 0; i < data.length; i++){
    dataArray.push({"label":data[i][0], "y":data[i][12]})
  } 
  
  var chart = new CanvasJS.Chart("barchart", {
    animationEnabled: true,
    title:{
      text: "Unit Budget"              
    },
    data: [              
      { 
       type: "column",
       dataPoints: dataArray
     }
     ],
    axisY:{
      minimum: 0,
      prefix: "$ ",
      suffix:"/student"
    }     
    
  });
  chart.render();
}


/**Used to get data from server side 
 * @param does not have parameter 
 * function fetch the data and return a response of an array of data 
 * pass into the horizontal bar chart for plot the horizontal bar chart
*/
const getEmployeeData = () => {
  fetch('http://127.0.0.1:5000/employee_budget', {
    method:"GET",
    headers:{
      headers: {
        "Content-Type":"application/json"
      }
    }
  })
  .then(resp => resp.json())
  .then((data) =>
    horizontalbarchart(data)
  )
  .catch(error => 
    console.log(error))
}


/**Plot the horizontal bar graph 
 * @param data, type=array, receive data from server 
 * plot the data dynamically based on data from database 
*/
const horizontalbarchart = function (data) {
  const dataArray = []
  for(var i = 0; i < data.length; i++){
    if (data[i][4]!==0) {dataArray.push({"y":data[i][4], "label":data[i][0]}) }
  };



  var horizontal = document.getElementById("horizontal")
  var bar_chart = new CanvasJS.Chart(horizontal, {
    title:{
      text: "Budget for each employees"              
    },
    animationEnabled: true,
    data: [//array of dataSeries              
      { 
       type: "bar",
       dataPoints: dataArray
      }
    ],
    axisY:{
      minimum:0,
      prefix: "$",
    }     
    
  });
  bar_chart.render();
}

/**Used to get data from server side 
 * @param does not have parameter 
 * function fetch the data and return a response of an array of data 
 * pass into the graphing for plot the cluster bar chart
*/
const getWorkLoadData = function () {
  fetch('http://127.0.0.1:5000/workload', {
    method:"GET",
    headers:{
      headers: {
        "Content-Type":"application/json"
      }
    }
  })
  .then(resp => resp.json())
  .then((data) =>
    graphing(data)
  )
  .catch(error => 
    console.log(error))
}

/**Plot the cluster bar graph 
 * @param data, type=array, receive data from server 
 * plot the data dynamically based on data from database 
*/ 
const graphing =  function(data) {
  const workload = []
  const staffCost = []
  for(var i = 0; i < data.length; i++){
    workload.push({"label":data[i][0], "y":data[i][1]})
    staffCost.push({"label":data[i][0], "y":data[i][2]})
  };
  var stack = document.getElementById("stack")
  var stack_chart = new CanvasJS.Chart(stack, {

  theme: "light2",
  animationEnabled: true,
  title:{
    text: "Workload VS Total Cost"              
  },
  data: [    
    {     
      type: "column",
      axisYIndex: 0,
      name:"StaffCost",
      showInLegend: true,
      dataPoints: staffCost
    },
    { //dataSeries - second quarter

      type: "column",
      axisYIndex: 0,
      axisYType: "secondary",
      name:"Workload", 
      showInLegend: true,               
      dataPoints: workload
    }
  ],
/** Set axisY properties here*/
    axisY:[
      {
        title: "StaffCost",
        minimum:0,
        prefix: "$",
      }
    ],
    axisY2:[{
      suffix:"Hour",
      minimum:0,
      title: "Workload",
    }]   
  });

  stack_chart.render()
}

// function to check whether file has a specific extension 
function checkFile(send) {
  const extension = new Array('.xlsx','.xls'); 
  var fileExtension = send.value;
  // get the file extension 
  fileExtension = fileExtension.substring(fileExtension.lastIndexOf('.'));
  if (!extension.includes(fileExtension)) {
    alert("Invalid file selected, valid files are of " +extension.toString() + " types.")
    send.value='';
    return false;
  }
  else {
    return true
  }

}

// click to show user information 
function sampleInformation() {
  alert('Excel files includes files that have extension .xlsx and .xls. \
  For example: "file1.xlsx" or "file1.xls"')
}


getAllData()
getWorkLoadData()
getEmployeeData()
graphing()





