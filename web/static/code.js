$(document).ready(function(){
	(function fillSelectionsList() {
		const modes = ['ECB', 'CBC', 'CFB', 'OFB', 'CTR', 'OpenPGB', 'CCM', 'EAX', 'SIV', 'GCM', 'OCB']
		const disabled_modes = ['ECB', 'CBC', 'SIV']

		const selections_list = $('#selections_list')

		modes.forEach((mode) => {
			const selection = document.createElement('div')
			selection.setAttribute('class', 'mode_selection')

			const mode_input = document.createElement('input')
			const mode_label = document.createElement('label')

			mode_input.setAttribute('type', 'checkbox')
			mode_input.setAttribute('id', 'selection_' + mode)
			mode_input.setAttribute('name', 'AES_' + mode)

			if(!disabled_modes.includes(mode)){
				mode_input.setAttribute('checked', true)
			}

			mode_label.setAttribute('for', mode)
			mode_label.innerHTML = mode

			selection.append(mode_input)
			selection.append(mode_label)

			selections_list.append(selection)
		})
	})()

	function getSelectedModes() {
		const selected_modes_dom = $('.mode_selection input:checked').toArray()

		let selected_modes = []

		selected_modes_dom.forEach((mode) => {
			selected_modes.push(mode.name)
		})

		return selected_modes
	}

	function convertDictionaryToTable(dictionary) {
	    const table_view = document.createElement('div')
	    table_view.setAttribute('class', 'table_view')

	    const table = document.createElement('table')

	    table_view.append(table)

	    const keys = Object.keys(dictionary)

	    for(key in keys) {
	        const key_name = keys[key]
	        const row = document.createElement('tr')
	        const row_name = document.createElement('td')

	        row_name.innerHTML = key_name

	        row.append(row_name)

	        dictionary[key_name].forEach((data) => {
	            const data_td = document.createElement('td')
	            data_td.innerHTML = data
	            row.append(data_td)
	        })

	        table.append(row)
	    }

	    return table_view
	}

	$('#experiment_form').submit(function(e){
		e.preventDefault()

		const selected_modes = getSelectedModes()
		const keys_lengths = $('#keys_lengths').val().split(',').map((value) => {
		    return Number(value)
		})
		const max_message_length = Number($('#max_message_length').val())
		const amount_of_experiments = Number($('#amount_of_experiments').val())
		const duration_multiplier = Number($('#duration_multiplier').val())

		const form_data = {
		    data: JSON.stringify({
			    'selected_modes': selected_modes,
			    'keys_lengths': keys_lengths,
			    'max_message_length': max_message_length,
			    'amount_of_experiments': amount_of_experiments,
			    'duration_multiplier': duration_multiplier
			})
		}

		$.ajax({
		    url: '/process_form',
		    data: form_data,
		    success: function(json_data) {
		        $('#experiment_form').hide()
		        $('#result_block').show()

		        data = JSON.parse(json_data)

		        console.log(data)

		        $('#data_block').append(convertDictionaryToTable(data['data']))
		        $('#normalized_data_block').append(convertDictionaryToTable(data['normalized']))
		        //$('#characteristic_data_block').append(convertDictionaryToTable(data['characteristic']))
		        console.log(data['characteristic'])
		    }
		})
	})
})