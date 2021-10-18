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

/**
 * Build SearchParams to include supplied queries.
 * 
 * @param year The year when a report is created.
 * @param semester The semester a report targets to.
 * @param unitcode The Unit code a report targets to.
 * @param unitLevel Level of the unit.
 */
const buildSearchParams = (year, semester, unitcode, unitLevel) => {
  const queryParams = new URLSearchParams();
  if(year) {
    queryParams.append("year", year);
  }
  if(semester) {
    queryParams.append("semester", semester);
  }
  if(unitcode) {
    queryParams.append("unitcode", unitcode);
  }
  if(unitLevel) {
    queryParams.append("unitLevel", unitLevel);
  }

  return queryParams;
}


const buildCommentParams = (year, semester, unitcode) => {
  const requestParams = new URLSearchParams();
  if(year) {
    requestParams.append("year", year);
  }
  if(semester) {
    requestParams.append("semester", semester);
  }
  if(unitcode) {
    requestParams.append("unitcode", unitcode);
  }

  return requestParams;
}
/**
 * function fetch the data and return a response of an array of data 
 * pass into the window.onload for plot the bar graph
 * 
 * @param year The year when the report is created.
 * @param semester The semester which the report targets to.
 * @param unitcode The Unit code which the report targets to.
 * @param unitLevel Level of the unit.
 */ 
const getAllData = async(year, semester, unitcode, unitLevel) => {
  const queryParams = buildSearchParams(year, semester, unitcode, unitLevel);
  const result = await fetch('http://127.0.0.1:5000/get_all_data?' + queryParams, {
    method:"GET",
    headers:{
      headers: {
        "Content-Type":"application/json"
      }
    }
  });

  const data = await result.json();
  window.onload(data);
  return data;
}

/**
 * Plot a bar graph 
 * @param data type=array, receive data from server 
 * plot the data dynamically based on data from database 
 */
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
    data: [//array of dataSeries              
      { //dataSeries object

       /*** Change type "column" to "bar", "area", "line" or "pie"***/
       type: "column",
       dataPoints: dataArray
     }
     ],
    axisY:{
      minimum:0,
      prefix: "$",
    }     
    
  });
  chart.render();
}


/**
 * function fetch the data and return a response of an array of data 
 * pass into the horizontal bar chart for plot the horizontal bar chart
 * 
 * @param year The year when the report is created.
 * @param semester The semester which the report targets to.
 * @param unitcode The Unit code which the report targets to.
 * @param unitLevel Level of the unit.
 */ 
const getEmployeeData = (year, semester, unitcode, unitLevel) => {
  const queryParams = buildSearchParams(year, semester, unitcode, unitLevel);
  fetch('http://127.0.0.1:5000/employee_budget?' + queryParams, {
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


/**
 * Plot the horizontal bar graph 
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

/**
 * function fetch the data and return a response of an array of data 
 * pass into the graphing for plot the cluster bar chart 
 *
 * @param year The year when the report is created.
 * @param semester The semester which the report targets to.
 * @param unitcode The Unit code which the report targets to.
 * @param unitLevel Level of the unit.
*/ 
const getWorkLoadData = function (year, semester, unitcode, unitLevel) {
  const queryParams = buildSearchParams(year, semester, unitcode, unitLevel);
  fetch('http://127.0.0.1:5000/workload?' + queryParams, {
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

/**
 * Plot the cluster bar graph 
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


/**
 * function that take an event when user click 
 * used the jquery function toggle() to display and hide 
 *
 * @param click event  
*/ 
$('#comment').on('click', function(event) {
  event.preventDefault()
  $('#table_comments').toggle();
  $('#unitcodes').toggle();
  $('#unitcodelabels').toggle();
  $('#years').toggle();
  $('#yearlabels').toggle();
  $('.clear').toggle();
  $('#semester').toggle();
  $('#semesterlabel').toggle();
})

/**
 * function take an array of data  
 * array data that pass in the create table to create the table dynamically 
 *
 * @param an array of the data 
*/ 
function create_table(data) {
  const name = document.getElementById('table_comments')
  for(var i = 0; i < data.length; i++)
  {
    var newRow = name.insertRow(name.length);
    for(var j = 0; j < data[i].length; j++) {
      var cell = newRow.insertCell(j);
      cell.innerHTML = data[i][j]
    }
  }
}  

/**
 * function fetch the data with comment and return a response of an array of data 
 * pass into the create table to create the table 
 *
 * @param year which is the input user what year they want .
 * @param semester which is the input user what semester what they want 
 * @param unitcode which is the input user what unitcode what they want.
*/ 
var sendComment = async(year,semester, unitcode) => {
  const requestParams = buildCommentParams(year, semester, unitcode);
  const result = await fetch('http://127.0.0.1:5000/comment?' + requestParams , {
    method:"GET",
    headers:{
      headers: {
        "Content-Type":"application/json"
      }
    }
  })
  const data = await result.json()
  create_table(data)
  return data;
}


/**
 * function take when button is clicked, 
 * it will remove the table
 * and it will remove unitcodes, years and semester input 
 *
 * @param take no parameter 
*/ 
function clearFunction() {
  $("#table_comments tr>td").remove();
  document.getElementById('unitcodes').value='';
  document.getElementById('years').value='';
  document.getElementById('semester').value='';
}


/**
 * function that check when user enter in the input, 
 * and it will take the value and pass into the sendComment function
 * and it will remove unitcodes, years and semester input 
 *
 * @param take no parameter 
*/ 
const updateComment = async() => {
  const yearValue = $("#years").val().toString();
  const semesterValue = $("#semester").val().toString();
  const unitValue = $("#unitcodes").val().toString();

  sendComment(yearValue,semesterValue,unitValue)
}

/**
 * function that handle click event by 
 * detect the enter key  
 *
 * @param click event  
*/ 
const handleClick = (e)=>{
  if(e.keyCode === 13){
    updateComment()
  }
}

/**
 * function that handle click event by 
 * detect the delete key  
 *
 * @param take no parameter 
*/ 
const unit= document.getElementById('unitcodes');
const year = document.getElementById('years')
const semester = document.getElementById('semester')
unit.onkeydown = function() {
    var key = event.keyCode || event.charCode
    if( key == 8 || key == 46 )
      $("#table_comments tr>td").remove();
};
year.onkeydown = function() {
  var key = event.keyCode || event.charCode
  if( key == 8 || key == 46 )
    $("#table_comments tr>td").remove();
};
semester.onkeydown = function() {
  var key = event.keyCode || event.charCode
  if( key == 8 || key == 46 )
    $("#table_comments tr>td").remove();
};



getAllData()
getWorkLoadData()
getEmployeeData()
graphing()








