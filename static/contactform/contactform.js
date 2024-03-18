jQuery(document).ready(function ($) {
  "use strict";

  //Contact
  $("form.contactForm").submit(function () {
    var f = $(this).find(".form-group"),
      ferror = false,
      emailExp = /^[^\s()<>@,;:\/]+@\w[\w\.-]+\.[a-z]{2,}$/i;

    f.children("input").each(function () {
      // run all inputs

      var i = $(this); // current input
      var rule = i.attr("data-rule");

      if (rule !== undefined) {
        var ierror = false; // error flag for current input
        var pos = rule.indexOf(":", 0);
        if (pos >= 0) {
          var exp = rule.substr(pos + 1, rule.length);
          rule = rule.substr(0, pos);
        } else {
          rule = rule.substr(pos + 1, rule.length);
        }

        switch (rule) {
          case "required":
            if (i.val() === "") {
              ferror = ierror = true;
            }
            break;

          case "minlen":
            if (i.val().length < parseInt(exp)) {
              ferror = ierror = true;
            }
            break;

          case "email":
            if (!emailExp.test(i.val())) {
              ferror = ierror = true;
            }
            break;

          case "checked":
            if (!i.is(":checked")) {
              ferror = ierror = true;
            }
            break;

          case "regexp":
            exp = new RegExp(exp);
            if (!exp.test(i.val())) {
              ferror = ierror = true;
            }
            break;
        }
        i.next(".validation")
          .html(
            ierror
              ? i.attr("data-msg") !== undefined
                ? i.attr("data-msg")
                : "wrong Input"
              : ""
          )
          .show("blind");
      }
    });
    f.children("textarea").each(function () {
      // run all inputs

      var i = $(this); // current input
      var rule = i.attr("data-rule");

      if (rule !== undefined) {
        var ierror = false; // error flag for current input
        var pos = rule.indexOf(":", 0);
        if (pos >= 0) {
          var exp = rule.substr(pos + 1, rule.length);
          rule = rule.substr(0, pos);
        } else {
          rule = rule.substr(pos + 1, rule.length);
        }

        switch (rule) {
          case "required":
            if (i.val() === "") {
              ferror = ierror = true;
            }
            break;

          case "minlen":
            if (i.val().length < parseInt(exp)) {
              ferror = ierror = true;
            }
            break;
        }
        i.next(".validation")
          .html(
            ierror
              ? i.attr("data-msg") != undefined
                ? i.attr("data-msg")
                : "wrong Input"
              : ""
          )
          .show("blind");
      }
    });
    if (ferror) return false;
    else var str = $(this).serialize();
    var action = $(this).attr("action");
    if (!action) {
      action = "contactform/contactform.php";
    }
    $.ajax({
      type: "POST",
      url: action,
      data: str,
      success: function (msg) {
        // If server response is "OK"
        if (msg == "OK") {
          console.log("Form Submission Successful"); // Log successful form submission
          $("#sendmessage").addClass("show");
          $("#errormessage").removeClass("show");
          $(".contactForm").find("input, textarea").val("");
        }
        // If server response indicates another error condition
        else if (msg == "OK2") {
          console.log("Form Submission Successful"); // Log successful form submission
          $("#sendmessage").html(
            "Thank You For Contacting Us Again. We Will Contact You Soon."
          );
          $("#sendmessage").addClass("show");
          $("#errormessage").removeClass("show");
          $(".contactForm").find("input, textarea").val("");
        }
        // If server response does not match any expected condition
        else {
          console.log("Form Submission Failed With Error:", msg); // Log error message
          $("#sendmessage").removeClass("show");
          $("#errormessage").addClass("show");
          // $("#errormessage").html(msg);
          $(".contactForm").find("input, textarea").val("");
        }
      },
    });
    // $.ajax({
    //   type: "POST",
    //   url: action,
    //   data: str,
    //   success: function (msg) {
    //     // Display success message and clear form fields
    //     console.log("Server response:", msg); // Log server response
    //     if (msg == "OK") {
    //       console.log("Form submission successful"); // Log successful form submission
    //       $("#sendmessage").addClass("show");
    //       $("#errormessage").removeClass("show");
    //       $(".contactForm").find("input, textarea").val("");
    //     } else {
    //       // Display error message
    //       console.log("Form submission failed with error:", msg); // Log error message
    //       $("#sendmessage").removeClass("show");
    //       $("#errormessage").addClass("show");
    //       $("#errormessage").html(msg);
    //     }
    //   },
    // });

    return false;
  });
});
