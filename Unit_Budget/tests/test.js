const Application = require('spectron').Application;
const path = require('path');
const chai = require('chai');
const chaiAsPromised = require('chai-as-promised');
var assert = require('assert');


var electronPath = require("electron")

// for getting the path for th app 
var appPath = path.join(__dirname, '..');

global.before(function () {
  chai.should();
  chai.use(chaiAsPromised);
});

// create a new constructor for Application 
const app = new Application({
  path: electronPath,
  args: [appPath],
});


describe('Application Launch', function () {
  /**Used to set up the test 
   * for each running, it starts the application 
  */
  beforeEach(function () {
    return app.start();
  });

  /**Used after running the test
   * for each running, it starts the application 
  */
  afterEach(function () {
      return app.stop()
  });

  /**create a test to check whether the window open correctly
   * @param done, which is used for asynchronouse, call done when the function is finised, 
   * return a promise 
  */
  it('opens a window', function (done) {
    app.client.getWindowCount().then(function (count) {
      assert.equal(count, 2);
      done();
    })
    .catch(err => done(err))
  })

  /**create a test to check whether element of id summary in HTML is Summary Report
   * @param done, which is used for asynchronouse, call done when the function is finised, 
   * return a promise 
  */
  it('Navigate to Summary report', function (done) {
    app.client.$('#summary').then(function (element) {
      element.getText().then(function (text) {
        (text,"Summary Report")
      })
      done()
    })
    .catch(err => done(err))
  })  
});
