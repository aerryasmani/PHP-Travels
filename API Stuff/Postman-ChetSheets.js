//General Structure Script for postman

//Create Test Case
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

//Used to assert different aspects of the response or other values.
pm.test("Request Method is GET",function{
    pm.expect(pm.request.method).to.eql("GET");
});

//Access the response object, allowing you to inspect the response data.
pm.test("Response time is less than 500ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(500);
});

//Access the request object, allowing you to inspect the request details.
pm.test("Request method is GET", function () {
    pm.expect(pm.request.method).to.eql("GET");
});

//Manipulate the Environment
pm.environment.set("token", "your_token_here");
pm.test("Token is set", function () {
    pm.expect(pm.environment.get("token")).to.eql("your_token_here");
});

//Manipulate collection variables.
pm.collectionVariables.set("base_url", "https://api.example.com");
pm.test("Base URL is set", function () {
    pm.expect(pm.collectionVariables.get("base_url")).to.eql("https://api.example.com");
});

//Manipulate global variables
pm.globals.set("user_id", "12345");
pm.test("Global variable user_id is set", function () {
    pm.expect(pm.globals.get("user_id")).to.eql("12345");
});
