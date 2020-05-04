function showExtras(name, options_nb) {
    document.addEventListener('DOMContentLoaded', () => {
        if (name === 'Sub') {
            const sub_label = "Optionally chose your extras for +0.50$ each";
            document.querySelector('label').innerHTML = sub_label;
            document.querySelector('select').size = 5;
        } 
        // When name is Regular Pizza or Sicilian Pizza
        else {
            place_order = document.getElementById('place_order');
            place_order.disabled = true;
            all_options = document.querySelector('select');
    
            all_options.addEventListener('click', function() {
                if (all_options.selectedOptions.length === options_nb)
                    place_order.disabled = false;
                else
                    place_order.disabled = true;
            });
        }
    });
}

function Add_to_cart_ok() {
    alert('The meal has been added to your shopping cart')
}