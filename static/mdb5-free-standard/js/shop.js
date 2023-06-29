function addUrlParameters(param, value){
    var params = new URLSearchParams(window.location.search);
    params.set(param, value);
    window.location.search = params.toString();
}

function removeUrlParameter(param){
    var params = new URLSearchParams(window.location.search);
    params.delete(param);
    window.location.search = params.toString();
}