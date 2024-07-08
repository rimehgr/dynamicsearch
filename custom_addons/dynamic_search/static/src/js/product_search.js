
odoo.define('your_module.product_search', function(require) {
    'use strict';

    var rpc = require('web.rpc');
    var core = require('web.core');

    $(document).ready(function() {
        $('input[name="search"]').on('input', function() {
            var search_query = $(this).val();
            rpc.query({
                model: 'product.product',
                method: 'name_search',
                args: [search_query],
            }).then(function(results) {
                // Update UI with new search results

                var $tree = $('.oe_searchview_results').find('.o_list_view');
                $tree.empty();
                results.forEach(function(result) {
                    var $row = $('<tr>');
                    $row.append($('<td>').text(result.name));
                    $row.append($('<td>').text(result.default_code));
                    $row.append($('<td>').text(result.description));
                    $tree.append($row);
                });
            });
        });
    });

});
