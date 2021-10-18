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
   * @param done, which is used for asynchronouse, call done when the function is finished, 
   * return a promise 
  */
  it('opens a window', function (done) {
    app.client.getWindowCount().then(function (count) {
      assert.equal(count, 1);
      done();
    })
    .catch(err => done(err))
  })

  /**create a test to check the title of the project templates
   * @param None
   * return a response and check whether it is equal to the actual template titles
  */
  it('title', function () {
    return app.client.getTitle().should.eventually.equal('Unit Budget Planner');
   });

  /**create a test to check whether element of id summary in HTML is Summary Report
   * @param done, which is used for asynchronouse, call done when the function is finished, 
   * return a promise 
  */
  it('get the element name', function (done) {
    app.client.$('#summary').then(function (element) {
      element.getText().then(function (text) {
        assert.equal(text,"Summary Report")
      })
      done()
    })
    .catch(err => done(err))
  })  

  /**create a test to check whether when it click, redirect to summary report page
   * @param done, which is used for asynchronouse, call done when the function is finished, 
   * return a promise 
  */
  it("navigate to summary report", function (done)  {
    app.client.$('#summary').then(function (element) {
      element.click()
      setTimeout(done, 1500);
    })
    .catch(err => done(err))
  })

  /**create a test to check whether when it click, redirect to summary report page and back to main page
   * @param done, which is used for asynchronouse, call done when the function is finished, 
   * return a promise 
  */
  it("back to the main page", function (done)  {
    app.client.$('#summary').then(function (element) {
      element.click().then(function(done) {
        app.client.$('#back').then(function(back) {
          back.click()
          done()
        })
      })
      setTimeout(done, 1500);
    })
    .catch(err => done(err))
  })

  /**create a test to check whether comment button is click
   * @param done, which is used for asynchronouse, call done when the function is finished, 
   * return a promise 
  */
   it("comment button", function (done)  {
    app.client.$('#summary').then(function (element) {
      element.click().then(function(done) {
        app.client.$('#comment').then(function(comment) {
          comment.click()
          done()
        })
      })
      setTimeout(done, 1500);
    })
    .catch(err => done(err))
  })

  /**create a test to check the input value and click enter
   * @param done, which is used for asynchronouse, call done when the function is finished, 
   * return a promise 
  */

  it("input values for comment", function (done)  {
    app.client.$('#summary').then(function (element) {
      element.click().then(function(done) {
        app.client.$('#comment').then(function(comment) {
          comment.click().then(function(done) {
            app.client.$('#unitcodes').then(function(input) {
              input.setValue('CITS5503').then(function(done) {
                app.client.keys("Enter")
                done()
              })
            })
            done()
          })
          done()
        })
      })
      setTimeout(done, 1900);
    })
    .catch(err => done(err))
  })

  /**create a test to check the input value and click enter and clear using the clear function
   * @param done, which is used for asynchronouse, call done when the function is finished, 
   * return a promise 
  */

   it("input values for comment", function (done)  {
    app.client.$('#summary').then(function (element) {
      element.click().then(function(done) {
        app.client.$('#comment').then(function(comment) {
          comment.click().then(function(done) {
            app.client.$('#unitcodes').then(function(input) {
              input.setValue('CITS5503').then(function(done) {
                app.client.keys("Enter").then(function(done) {
                  app.client.$('#clear').then(function(clear) {
                    clear.click()
                    done()
                  })
                })
                setTimeout(done, 1500);
              })
            })
            done()
          })
          done()
        })
      })
      setTimeout(done, 2600);
    })
    .catch(err => done(err))
  })



  /**create a test to when the users click the filter button and choose the option, it should update the chart and table
   * @param done, which is used for asynchronouse, call done when the function is finished, 
   * return a promise 
  */
  it("filter button", function (done)  {
    app.client.$('#summary').then(function (element) {
      element.click().then(function(done) {
        app.client.$('#filter').then(function(filter) {
          filter.click()
          done()
        })
      })
      setTimeout(done, 1500);
    })
    .catch(err => done(err))
  })


  /**create a test to when the users click the filter button
   * @param done, which is used for asynchronouse, call done when the function is finished, 
   * return a promise 
  */
  it("Check filter and choose option", function (done)  {
    app.client.$('#summary').then(function (element) {
      element.click().then(function(done) {
        app.client.$('#filter').then(function(filter) {
          filter.click().then(function(done) {
            app.client.$('#_year').then(function(dropdown) {
              dropdown.click().then(function(done) {
                dropdown.selectByVisibleText('2020')
                done()
              })
            })
            done()
          })
          done()
        })
      })
      done()
    })
    .catch(err => done(err))
  })




  /**create a test to check whether when it click, the button of Head of Finance get the element and compare the element
   * @param done, which is used for asynchronouse, call done when the function is finished, 
   * return a promise 
  */
  //  it("select role as Head of Finance", function (done)  {
  //   app.client.$('#Head of Finance').then (function (element) {
  //     element.click().then(function(text) {
  //       assert.equal(text,"You are the Head of Finance.")
  //     })
  //     done()
  //   })
  //   .catch(err => done(err))
  // })
});
  