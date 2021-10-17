const {app, BrowserWindow} = require('electron')
const path = require('path')
require("electron-reload")(__dirname)

function createWindow () {
  // Create the browser window.
  const mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js')
    }
  })

  mainWindow.loadFile('./dist/index.html')

  var pyshell =  require('python-shell');
  pyshell.run('./Python_File/route.py',  function  (err, results)  {
  if  (err)  console.log(err);
  }); 

  // Initializing the Database
  // const sqlite3 = require('sqlite3').verbose();
  // let db = new sqlite3.Database('./DataBase/Unit_Budget.db', (err) => {
  //   if (err) {
  //     console.error(err.message);
  //  }
  //   console.log('Connected to the Unit Budget database.');
  // });

  // const DBStructurefile = require('child_process').spawn('python',['./Python_file/Create_Table.py']);
  //   DBStructurefile.stdout.on('data',function(data){
  //     console.log("DB Info: ",data.toString('utf8'));
  //   });

  // // Insert Dummy Unit Data
  // const InsertUnitData = require('child_process').spawn('python',['./Python_file/Insert_Unit_Data.py']);
  //   InsertUnitData.stdout.on('data',function(data){
  //     console.log("DB Info: ",data.toString('utf8'));
  //   });

  // // Test DB Connection
  // db.serialize(() => {
  //   db.each(`SELECT * 
  //            FROM Unit`, (err, row) => {
  //     if (err) {
  //      console.error(err.message);
  //    }
  //     console.log(row.UnitID + "\t" + row.UnitCode + "\t" + row.Semester + "\t" + row.Year);
  //   });
  // });

  // and load the index.html of the app.

  // mainWindow.setFullScreen(true);
  mainWindow.maximize();

  // Open the DevTools.
  //mainWindow.webContents.openDevTools()
}

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.whenReady().then(() => {
  createWindow()

  app.on('activate', function () {
    // On macOS it's common to re-create a window in the app when the
    // dock icon is clicked and there are no other windows open.
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
  })
})

// Quit when all windows are closed, except on macOS. There, it's common
// for applications and their menu bar to stay active until the user quits
// explicitly with Cmd + Q.
app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') app.quit()
})

// In this file you can include the rest of your app's specific main process
// code. You can also put them in separate files and require them here.