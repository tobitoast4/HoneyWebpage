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

function addAndRemoveMultipleUrlParameters(params_to_add_dict, params_to_remove_list){
    console.log(params_to_add_dict);
    console.log(params_to_remove_list);

    var params = new URLSearchParams(window.location.search);

    for (const [param, value] of Object.entries(params_to_add_dict)) {
        params.set(param, value);
    }

    for (const param of params_to_remove_list) {
        console.log(param);
        params.delete(param);
    }

    window.location.search = params.toString();
}