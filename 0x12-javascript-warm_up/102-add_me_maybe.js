exports.addMeMaybe = function (number, theFunction) {
  if (!isNaN(parseInt(number))) {
    theFunction(number + 1);
  }
};
