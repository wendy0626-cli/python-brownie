// No License
pragma solidity ^0.8.0;

contract FooBar {

    string identifier;

    constructor() {
        identifier = "FooBar001";
    }

    event HelloCalled(
        address operator,
        string funcMsg
    );

    function testFunc() public {
        emit HelloCalled(msg.sender, "Hello World!");
    }
}