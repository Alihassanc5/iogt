MEDIA_CHOOSER_MODAL_ONLOAD_HANDLERS = {
    'chooser': function(modal, jsonData) {
        var searchUrl = $('form.media-search', modal.body).attr('action');

        /* currentTag stores the tag currently being filtered on, so that we can
        preserve this when paginating */
        var currentTag;

        function ajaxifyLinks (context) {
            $('a.media-choice', context).on('click', function(e) {
                modal.loadUrl(this.href);
                e.preventDefault();
            });

            $('.pagination a', context).on('click', function(e) {
                var page = this.getAttribute("data-page");
                setPage(page);
                e.preventDefault();
            });
        }

        function fetchResults(requestData) {
            $.ajax({
                url: searchUrl,
                data: requestData,
                success: function(data, status) {
                    $('#search-results').html(data);
                    ajaxifyLinks($('#search-results'));
                }
            });
        }

        function search() {
            /* Searching causes currentTag to be cleared - otherwise there's
            no way to de-select a tag */
            currentTag = null;
            fetchResults({
                q: $('#id_q').val(),
                collection_id: $('#collection_chooser_collection_id').val()
            });
            return false;
        }

        function setPage(page) {
            params = {p: page};
            if ($('#id_q').val().length){
                params['q'] = $('#id_q').val();
            }
            if (currentTag) {
                params['tag'] = currentTag;
            }
            params['collection_id'] = $('#collection_chooser_collection_id').val();
            fetchResults(params);
            return false;
        }

        ajaxifyLinks(modal.body);

        $('form.media-upload', modal.body).on('submit', function() {
            alert('Videos and audios aren\'t support in facebook free basics.');

            var formdata = new FormData(this);

            if ($('#id_title', modal.body).val() == '') {
                var li = $('#id_title', modal.body).closest('li');
                if (!li.hasClass('error')) {
                    li.addClass('error');
                    $('#id_title', modal.body).closest('.field-content').append('<p class="error-message"><span>This field is required.</span></p>')
                }
                setTimeout(cancelSpinner, 500);
            } else {
                $.ajax({
                    url: this.action,
                    data: formdata,
                    processData: false,
                    contentType: false,
                    type: 'POST',
                    dataType: 'text',
                    success: modal.loadResponseText,
                    error: function(response, textStatus, errorThrown) {
                        message = jsonData['error_message'] + '<br />' + errorThrown + ' - ' + response.status;
                        $('#upload').append(
                            '<div class="help-block help-critical">' +
                            '<strong>' + jsonData['error_label'] + ': </strong>' + message + '</div>');
                    }
                });
            }

            return false;
        });

        $('form.media-search', modal.body).on('submit', search);

        $('#id_q').on('input', function() {
            clearTimeout($.data(this, 'timer'));
            var wait = setTimeout(search, 200);
            $(this).data('timer', wait);
        });
        $('#collection_chooser_collection_id').on('change', search);
        $('a.suggested-tag').on('click', function() {
            currentTag = $(this).text();
            $('#id_q').val('');
            fetchResults({
                'tag': currentTag,
                collection_id: $('#collection_chooser_collection_id').val()
            });
            return false;
        });

        function populateTitle(context) {
            // Note: There are two inputs with `#id_title` on the page.
            // The page title and media title. Select the input inside the modal body.
            var fileWidget = $('#id_file', context);
            fileWidget.on('change', function () {
                var titleWidget = $('#id_title', context);
                var title = titleWidget.val();
                if (title === '') {
                    // The file widget value example: `C:\fakepath\media.jpg`
                    var parts = fileWidget.val().split('\\');
                    var fileName = parts[parts.length - 1];
                    titleWidget.val(fileName);
                }
            });
        }

        populateTitle(modal.body);

        /* Add tag entry interface (with autocompletion) to the tag field of the media upload form */
        $('#id_tags', modal.body).tagit({
            autocomplete: {source: jsonData['tag_autocomplete_url']}
        });
    },
    'media_chosen': function(modal, jsonData) {
        modal.respond('mediaChosen', jsonData['result']);
        modal.close();
    },
    'select_format': function(modal) {
        $('form', modal.body).on('submit', function() {
            var formdata = new FormData(this);

            $.post(this.action, $(this).serialize(), modal.loadResponseText, 'text');

            return false;
        });
    }
};
