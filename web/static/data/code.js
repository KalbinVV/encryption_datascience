$(document).ready(function(){
    data_id = get_data_id()

    function convertDictionaryToTable(dictionary, count) {
        const table_view = document.createElement('div')
	    table_view.setAttribute('class', 'table_view')

	    const table = document.createElement('table')

	    table_view.append(table)

	    const entries = Object.entries(dictionary)

        // Render rows names

        const row_names = document.createElement('tr')

        const values_counts = entries[0][1].length

        for(let i = 0; i < entries.length; i++) {
            const row_name = entries[i][0]

            const row_td = document.createElement('td')
            row_td.innerHTML = row_name

            row_names.append(row_td)
        }

        table.append(row_names)

        // Print values

        let current_index = 0

        while(current_index < values_counts) {
            const value_row = document.createElement('tr')

            for(let i = 0; i < entries.length; i++) {
                const value_td = document.createElement('td')
                value_td.innerHTML = entries[i][1][current_index]
                value_row.append(value_td)
            }

            table.append(value_row)

            current_index++
        }

        return table_view
	}

    $.ajax({
       url: '/get_data',
       data: 'id='+data_id,
       success: function(json_data) {
        data = JSON.parse(json_data)

        $('#data_block').append(convertDictionaryToTable(data['data']))
		$('#normalized_data_block').append(convertDictionaryToTable(data['normalized']))
		$('#characteristic_data_block').append(convertDictionaryToTable(data['characteristic']))
		$('#correlation_data_block').append(data['correlation'])
       }
    })
})