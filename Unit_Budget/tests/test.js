const Application = require('spectron').Application;
const path = require('path');
const chai = require('chai');
const chaiAsPromised = require('chai-as-promised');
var assert = require('assert');


var electronPath = require("electron")


var appPath = path.join(__dirname, '..');

global.before(function () {
  chai.should();
  chai.use(chaiAsPromised);
});

const app = new Application({
  path: electronPath,
  args: [appPath],
});


describe('Application Launch', function () {
  beforeEach(function () {
    chaiAsPromised.transferPromiseness = app.transferPromiseness;
    return app.start();
  });

  afterEach(function () {
      return app.stop()
  });

  it('opens a window', function (done) {
    app.client.getWindowCount().then(function (count) {
      assert.equal(count, 2);
      done();
    })
    .catch(err => done(err))
  })

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
