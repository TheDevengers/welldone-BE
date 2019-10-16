var dateOrderList = document.querySelector('#date_order');
var params = getAllUrlParams();
params.hasOwnProperty('order') && params['order'] === 'date'
  ? dateOrderList.selectedIndex = 1
  : dateOrderList.selectedIndex = 0

dateOrderList.addEventListener('change', (e) => {
  params['order'] = dateOrderList.value
  var queryString = Object.keys(params).map(function (key) {
    return key + '=' + params[key]
  }).join('&');
  location.replace(location.pathname + '?' + queryString)
})
