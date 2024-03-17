angular
  .module('KRRclass', ['chart.js'])
  .controller('MainCtrl', ['$scope', '$http', mainCtrl]);

function mainCtrl($scope, $http) {
  $scope.startMyAwesomeApp = function () {
    $scope.myDisplayMessage =
      'Welcome to my awesome Web Application called: ' + $scope.myInputAppName;
    $scope.mySparqlEndpoint = $scope.myInputEndPoint;
    $scope.mySparqlQuery = encodeURI($scope.myInputQuery).replace(/#/g, '%23');

    $http({
      method: 'GET',
      url: $scope.mySparqlEndpoint + '?query=' + $scope.mySparqlQuery,
      headers: {
        Accept: 'application/sparql-results+json',
        'Content-Type': 'application/sparql-results+json',
      },
    })
      .success(function (data, status) {
        $scope.myDynamicLabels = [];
        $scope.myDynamicData = [];

        // now iterate on the results
        const headers = data.head.vars;
        angular.forEach(data.results.bindings, function (val) {
          $scope.myDynamicLabels.push(val[headers[0]].value);
          $scope.myDynamicData.push(
            parseInt(val[headers[1]].value.replace(/,/g, ''))
          );
        });
      })
      .error(function (error) {
        console.log('Error running the input query!' + error);
      });
  };
}
