const sum = $('#sum')
const subtract = $('#subtract')
const multiply = $('#multiply')
const divide = $('#divide')

const answer = $('#answer')

const A = $('#a')
const B = $('#b')

sum.on('click', function () {
    $.ajax({
        url: "http://127.0.0.1:8000/api/add/",
        method: 'post',
        dataType: "json",
        contentType: "application/json",
        data: JSON.stringify({A: A.val(), B: B.val()}),
        success: function (response) {
            answer.removeClass('alert-danger')
            answer.addClass('alert-success')
            const res = response.answer
            answer.text('Answer: ' + res)
        },
        error: function (response) {
            answer.addClass('alert-danger')
            const message = response.responseText
            const err = JSON.parse(message)
            answer.text(err.error)
        }
    });
})

subtract.on('click', function () {
    $.ajax({
        url: "http://127.0.0.1:8000/api/subtract/",
        method: 'post',
        dataType: "json",
        contentType: "application/json",
        data: JSON.stringify({A: A.val(), B: B.val()}),
        success: function (response) {
            answer.removeClass('alert-danger')
            answer.addClass('alert-success')
            const res = response.answer
            answer.text('Answer: ' + res)
        },
        error: function (response) {
            answer.addClass('alert-danger')
            const message = response.responseText
            const err = JSON.parse(message)
            answer.text(err.error)
        }
    });
})

multiply.on('click', function () {
    $.ajax({
        url: "http://127.0.0.1:8000/api/multiply/",
        method: 'post',
        dataType: "json",
        contentType: "application/json",
        data: JSON.stringify({A: A.val(), B: B.val()}),
        success: function (response) {
            const res = response.answer
            answer.removeClass('alert-danger')
            answer.addClass('alert-success')
            answer.text('Answer: ' + res)
        },
        error: function (response) {
            answer.addClass('alert-danger')
            const message = response.responseText
            const err = JSON.parse(message)
            answer.text(err.error)
        }
    });
})

divide.on('click', function () {
    $.ajax({
        url: "http://127.0.0.1:8000/api/divide/",
        method: 'post',
        dataType: "json",
        contentType: "application/json",
        data: JSON.stringify({A: A.val(), B: B.val()}),
        success: function (response) {
            const res = response.answer
            answer.removeClass('alert-danger')
            answer.addClass('alert-success')
            answer.text('Answer: ' + res)
        },
        error: function (response) {
            answer.addClass('alert-danger')
            const message = response.responseText
            const err = JSON.parse(message)
            answer.text(err.error)
        }
    });
})

