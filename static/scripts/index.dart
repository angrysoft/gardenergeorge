import 'dart:html';

class AllAllowedUrlPolicy implements UriPolicy {
  AllAllowedUrlPolicy();

  //RegExp regex = new RegExp(r'(?:http://|https://|//).*');

  bool allowsUri(String uri) {
    return true;
  }
}

void main() {
HttpRequest.getString('/reviews')
    .then((String reviews) {
      DivElement reviewsRows = querySelector('#reviews-rows');
      NodeValidatorBuilder val = new NodeValidatorBuilder();
      val
        ..allowHtml5()
        ..allowInlineStyles()
        ..allowNavigation(new AllAllowedUrlPolicy())
        ..allowTextElements()
        ..allowImages(new AllAllowedUrlPolicy());
      reviewsRows.setInnerHtml(reviews, validator: val);
    })
    .catchError((Error error) {
      print(error.toString());
    });
}