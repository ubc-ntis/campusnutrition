var data_search = {}

$(document).ready(function() {
    // empty search parameters
    resetFilters();

    // fill in select options
    getCategories();
    getNames();

    $("#name").on('change', function() {
        if(this.value == "all") {
            data_search['name'] = "";
            console.log(data_search['name']);
        } else {
            data_search['name'] = this.value;
            console.log(data_search['name']);
        }

        getData();
    });

    $("#category").on('change', function() {
        if(this.value == "all") {
            data_search['category'] = "";
            console.log(data_search['category']);
        } else {
            data_search['category'] = this.value;
            console.log(data_search['category']);
        }

        getData();
    });
});

function getData() {
    let url = $('#list-data').attr("url");
    $.ajax({
        method: 'GET',
        url: url,
        data: data_search,
        beforeSend: function(){
            $("#no-results h1").html("Loading data...");
        },
        success: function (result) {
            console.log(result)
        },
        error: function (response) {
            $("#no-results h5").html("Something went wrong");
            //$("#list_data").hide();
        }
    });
}

function resetFilters() {
    data_search['name'] = '';
    data_search['category'] = '';
}

function getNames() {
    let url = $("#name").attr("url");
    $.ajax({
        method: 'GET',
        url: url,
        data: {},
        success: function(result) {
            names_option = "<option value='all' selected>All Names</option>";
            $.each(result["name"], function (a, b) {
                names_option += "<option>" + b + "</option>"
            });
            $("#name").html(names_option)
        },
        error: function(response) {
            console.log(response)
        }
    });
}

function getCategories() {
    let url = $("#category").attr("url");

    $.ajax({
        method: 'GET',
        url: url,
        data: {},
        success: function(result) {
            categories_option = "<option value='all' selected>All Categories</option>";
            $.each(result["category"], function (a, b) {
                categories_option += "<option>" + b + "</option>"
            });
            $("#category").html(categories_option)
        },
        error: function(response) {
            console.log(response)
        }
    });
}