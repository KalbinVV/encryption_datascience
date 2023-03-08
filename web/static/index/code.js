$(document).ready(function(){
    $.ajax({
        url: '/get_modes',
        success: function(data) {
            fillSelectionsList(JSON.parse(data))
        }
    })

	function fillSelectionsList(modes) {
		const selections_list = $('#selections_list')

		modes.forEach((mode) => {
		    mode_name = mode['name']
		    mode_status = mode['status']

			const selection = document.createElement('div')
			selection.setAttribute('class', 'mode_selection')

			const mode_input = document.createElement('input')
			const mode_label = document.createElement('label')

			mode_input.setAttribute('type', 'checkbox')
			mode_input.setAttribute('id', 'selection_' + mode_name)
			mode_input.setAttribute('name', mode_name)

			if(mode_status == 'Main'){
				mode_input.setAttribute('checked', true)
			} else if(mode_status == 'Dev') {
			    mode_label.setAttribute('class', 'unsupported_mode')
			}

			mode_label.setAttribute('for', mode_name)
			mode_label.innerHTML = mode_name

			selection.append(mode_input)
			selection.append(mode_label)

			selections_list.append(selection)
		})
	}

	function getSelectedModes() {
		const selected_modes_dom = $('.mode_selection input:checked').toArray()

		let selected_modes = []

		selected_modes_dom.forEach((mode) => {
			selected_modes.push(mode.name)
		})

		return selected_modes
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
		const max_amount_of_cycles = Number($('#max_amount_of_cycles').val())

		const form_data = {
		    data: JSON.stringify({
			    'selected_modes': selected_modes,
			    'keys_lengths': keys_lengths,
			    'max_message_length': max_message_length,
			    'amount_of_experiments': amount_of_experiments,
			    'duration_multiplier': duration_multiplier,
			    'max_amount_of_cycles': max_amount_of_cycles
			})
		}

        $('#experiment_form').hide()
        $('#waiting_block').show()

		$.ajax({
		    url: '/process_form',
		    data: form_data,
		    success: function(json_data) {
		        $('#waiting_block').hide()

		        data = JSON.parse(json_data)

		        if(data['status'] == false) {
		            $('#error_block').show()
		            $('#error_content').html(data['error'])
		        } else {
		            window.location.href = 'data/' + data['data_id']
		        }
		    }
		})
	})
})