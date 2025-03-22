import requests
import urllib.parse

class Request:
    def __init__(self, method, args):
        self.args = args
        self.method = method


    def search_books(self):
        search_query = urllib.parse.quote(self.search_var.get())
        url = f"https://www.googleapis.com/books/v1/volumes?q={search_query}&maxResults=5"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            print(data)  # Xử lý dữ liệu sách ở đây
        else:
            messagebox.showinfo("Error", "Failed to fetch data from Google Books API.")
# request = Request('GET', {'search': 'java'})

# if request.method == 'GET':
#     search = urllib.parse.quote(request.args.get('search', ''))
#     url = f"https://www.googleapis.com/books/v1/volumes?q={search}&maxResults=10"
#     response = requests.get(url)
#     # print(response.json())

#     if response.status_code == 200: # 200 means is status code susssecfull, 404 is not found
#         data = response.json()
#         for item in data.get('items', []):
#             volume_info = item.get('volumeInfo', {})
#             title = volume_info.get('title', 'N/A')
#             publisher = volume_info.get('publisher', 'N/A')
#             published_data = volume_info.get('publishedData', 'N/A')
#             author = volume_info.get('authors', ['N/A'])
#             rating = volume_info.get('averageRating', ['N/A'])
#             image_links = volume_info.get('imageLinks', {})
#             image = image_links.get('thumbnail') if 'thumbnail' in image_links else 'N/A'

#             print(title)
#             print(publisher)
#             print(published_data)
#             print(author)
#             print(rating)
#             print(image)
#             print('----------')



##########################
"""{
  "kind": "books#volumes",
  "totalItems": 565,
  "items": [
    {
      "kind": "books#volume",
      "id": "8T4hDQAAQBAJ",
      "etag": "QcqHf/LphY0",
      "selfLink": "https://www.googleapis.com/books/v1/volumes/8T4hDQAAQBAJ",
      "volumeInfo": {
        "title": "Pud Galvin",
        "subtitle": "Baseball's First 300-Game Winner",
        "authors": [
          "Brian Martin"
        ],
        "publisher": "McFarland",
        "publishedDate": "2016-09-29",
        "description": "Despite his outstanding pitching record, James Francis \"Pud\" Galvin (1856-1902) was largely forgotten after his premature death. During his 18-year career with Pittsburgh, Buffalo and St. Louis, he was one of the best-paid players in the game--but died penniless. The diminutive hurler was the first to reach 300 wins (and only four pitchers have amassed more). A determined researcher documented Galvin's record decades after his death and he was enshrined in the Hall of Fame in 1965 with 365 wins. This book is the first comprehensive biography of Galvin and his use of a testosterone-based concoction--with eye-popping results--which earned him newfound attention as a pioneer of performance enhancing drugs.",
        "industryIdentifiers": [
          {
            "type": "ISBN_13",
            "identifier": "9780786499779"
          },
          {
            "type": "ISBN_10",
            "identifier": "078649977X"
          }
        ],
        "readingModes": {
          "text": false,
          "image": true
        },
        "pageCount": 255,
        "printType": "BOOK",
        "categories": [
          "Sports & Recreation"
        ],
        "maturityRating": "NOT_MATURE",
        "allowAnonLogging": false,
        "contentVersion": "0.1.1.0.preview.1",
        "panelizationSummary": {
          "containsEpubBubbles": false,
          "containsImageBubbles": false
        },
        "imageLinks": {
          "smallThumbnail": "http://books.google.com/books/content?id=8T4hDQAAQBAJ&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
          "thumbnail": "http://books.google.com/books/content?id=8T4hDQAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
        },
        "language": "en",
        "previewLink": "http://books.google.com.vn/books?id=8T4hDQAAQBAJ&pg=PA28&dq=galvin&hl=&cd=1&source=gbs_api",
        "infoLink": "http://books.google.com.vn/books?id=8T4hDQAAQBAJ&dq=galvin&hl=&source=gbs_api",
        "canonicalVolumeLink": "https://books.google.com/books/about/Pud_Galvin.html?hl=&id=8T4hDQAAQBAJ"
      },
      "saleInfo": {
        "country": "VN",
        "saleability": "NOT_FOR_SALE",
        "isEbook": false
      },
      "accessInfo": {
        "country": "VN",
        "viewability": "PARTIAL",
        "embeddable": true,
        "publicDomain": false,
        "textToSpeechPermission": "ALLOWED",
        "epub": {
          "isAvailable": false
        },
        "pdf": {
          "isAvailable": true,
          "acsTokenLink": "http://books.google.com.vn/books/download/Pud_Galvin-sample-pdf.acsm?id=8T4hDQAAQBAJ&format=pdf&output=acs4_fulfillment_token&dl_type=sample&source=gbs_api"
        },
        "webReaderLink": "http://play.google.com/books/reader?id=8T4hDQAAQBAJ&hl=&source=gbs_api",
        "accessViewStatus": "SAMPLE",
        "quoteSharingAllowed": false
      },
      "searchInfo": {
        "textSnippet": "... \u003cb\u003eGalvin\u003c/b\u003e held the Atlantics to four hits to take his third win.35 On July 20, \u003cb\u003eGalvin\u003c/b\u003e was called upon again to pitch as Bradley moved to right field for an exhibition game in Lynn, Massachusetts, against the Live Oaks. \u003cb\u003eGalvin\u003c/b\u003e gave up five&nbsp;..."
      }
    },
    {
      "kind": "books#volume",
      "id": "EXNXeQmgA6kC",
      "etag": "Jxlc/VgKSC8",
      "selfLink": "https://www.googleapis.com/books/v1/volumes/EXNXeQmgA6kC",
      "volumeInfo": {
        "title": "Nomination of Michael Paul Galvin",
        "subtitle": "Hearing Before the Committee on Banking, Housing, and Urban Affairs, United States Senate, One Hundred First Congress, Second Session, on the Nomination of Michael Paul Galvin, of Illinois, to be an Assistant Secretary of Commerce for Export Administration, Vice Michael E. Zacharia, Resigned : April 25, 1990",
        "authors": [
          "United States. Congress. Senate. Committee on Banking, Housing, and Urban Affairs"
        ],
        "publishedDate": "1990",
        "industryIdentifiers": [
          {
            "type": "OTHER",
            "identifier": "STANFORD:36105045182347"
          }
        ],
        "readingModes": {
          "text": false,
          "image": true
        },
        "pageCount": 64,
        "printType": "BOOK",
        "maturityRating": "NOT_MATURE",
        "allowAnonLogging": false,
        "contentVersion": "0.6.6.0.full.1",
        "panelizationSummary": {
          "containsEpubBubbles": false,
          "containsImageBubbles": false
        },
        "imageLinks": {
          "smallThumbnail": "http://books.google.com/books/content?id=EXNXeQmgA6kC&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
          "thumbnail": "http://books.google.com/books/content?id=EXNXeQmgA6kC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
        },
        "language": "en",
        "previewLink": "http://books.google.com.vn/books?id=EXNXeQmgA6kC&pg=RA1-PA2&dq=galvin&hl=&cd=2&source=gbs_api",
        "infoLink": "https://play.google.com/store/books/details?id=EXNXeQmgA6kC&source=gbs_api",
        "canonicalVolumeLink": "https://play.google.com/store/books/details?id=EXNXeQmgA6kC"
      },
      "saleInfo": {
        "country": "VN",
        "saleability": "FREE",
        "isEbook": true,
        "buyLink": "https://play.google.com/store/books/details?id=EXNXeQmgA6kC&rdid=book-EXNXeQmgA6kC&rdot=1&source=gbs_api"
      },
      "accessInfo": {
        "country": "VN",
        "viewability": "ALL_PAGES",
        "embeddable": true,
        "publicDomain": true,
        "textToSpeechPermission": "ALLOWED",
        "epub": {
          "isAvailable": false,
          "downloadLink": "http://books.google.com.vn/books/download/Nomination_of_Michael_Paul_Galvin.epub?id=EXNXeQmgA6kC&hl=&output=epub&source=gbs_api"
        },
        "pdf": {
          "isAvailable": false
        },
        "webReaderLink": "http://play.google.com/books/reader?id=EXNXeQmgA6kC&hl=&source=gbs_api",
        "accessViewStatus": "FULL_PUBLIC_DOMAIN",
        "quoteSharingAllowed": false
      },
      "searchInfo": {
        "textSnippet": "... \u003cb\u003eGalvin\u003c/b\u003e, of Illinois, to be an Assistant Secretary of Commerce for Export Administration United States. Congress. Senate. Committee on Banking, Housing, and Urban Affairs. executive branch the authority to administer controls in the&nbsp;..."
      }
    },
    {
      "kind": "books#volume",
      "id": "LeTXjmSvZ1gC",
      "etag": "MiiOILsVQ0Y",
      "selfLink": "https://www.googleapis.com/books/v1/volumes/LeTXjmSvZ1gC",
      "volumeInfo": {
        "title": "Alternative Futures for the Department of Energy National Laboratories \"the Galvin Report\" and National Laboratories Need Clearer Missions and Better Management, a GAO Report to the Secretary of Energy",
        "subtitle": "Joint Hearing Before the Subcommittee on Basic Research and Subcommittee on Energy and Environment of the Committee on Science, U.S. House of Representatives, One Hundred Fourth Congress, First Session, March 9, 1995",
        "authors": [
          "United States. Congress. House. Committee on Science. Subcommittee on Basic Research"
        ],
        "publishedDate": "1995",
        "industryIdentifiers": [
          {
            "type": "OTHER",
            "identifier": "PSU:000024382779"
          }
        ],
        "readingModes": {
          "text": false,
          "image": true
        },
        "pageCount": 698,
        "printType": "BOOK",
        "categories": [
          "Business & Economics"
        ],
        "maturityRating": "NOT_MATURE",
        "allowAnonLogging": false,
        "contentVersion": "0.5.5.0.full.1",
        "panelizationSummary": {
          "containsEpubBubbles": false,
          "containsImageBubbles": false
        },
        "imageLinks": {
          "smallThumbnail": "http://books.google.com/books/content?id=LeTXjmSvZ1gC&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
          "thumbnail": "http://books.google.com/books/content?id=LeTXjmSvZ1gC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
        },
        "language": "en",
        "previewLink": "http://books.google.com.vn/books?id=LeTXjmSvZ1gC&pg=PA222&dq=galvin&hl=&cd=3&source=gbs_api",
        "infoLink": "https://play.google.com/store/books/details?id=LeTXjmSvZ1gC&source=gbs_api",
        "canonicalVolumeLink": "https://play.google.com/store/books/details?id=LeTXjmSvZ1gC"
      },
      "saleInfo": {
        "country": "VN",
        "saleability": "FREE",
        "isEbook": true,
        "buyLink": "https://play.google.com/store/books/details?id=LeTXjmSvZ1gC&rdid=book-LeTXjmSvZ1gC&rdot=1&source=gbs_api"
      },
      "accessInfo": {
        "country": "VN",
        "viewability": "ALL_PAGES",
        "embeddable": true,
        "publicDomain": true,
        "textToSpeechPermission": "ALLOWED",
        "epub": {
          "isAvailable": false,
          "downloadLink": "http://books.google.com.vn/books/download/Alternative_Futures_for_the_Department_o.epub?id=LeTXjmSvZ1gC&hl=&output=epub&source=gbs_api"
        },
        "pdf": {
          "isAvailable": false
        },
        "webReaderLink": "http://play.google.com/books/reader?id=LeTXjmSvZ1gC&hl=&source=gbs_api",
        "accessViewStatus": "FULL_PUBLIC_DOMAIN",
        "quoteSharingAllowed": false
      },
      "searchInfo": {
        "textSnippet": "... \u003cb\u003eGalvin\u003c/b\u003e Testimony 6 Energy a means to achieve part of its mission of science and technology . A better solution than corporatization is to use the recommendations of the \u003cb\u003eGalvin\u003c/b\u003e Report to make the Department a better steward of the&nbsp;..."
      }
    },
    {
      "kind": "books#volume",
      "id": "i5jX0-j_D-QC",
      "etag": "VnXGe58bqD8",
      "selfLink": "https://www.googleapis.com/books/v1/volumes/i5jX0-j_D-QC",
      "volumeInfo": {
        "title": "Galvin v. Detroit Steering Wheel & Windshield Co., 176 MICH 569 (1913)",
        "subtitle": "Brief",
        "publishedDate": "1913",
        "description": "41",
        "industryIdentifiers": [
          {
            "type": "OTHER",
            "identifier": "WSULL:WSUZ8224QK0V"
          }
        ],
        "readingModes": {
          "text": false,
          "image": true
        },
        "pageCount": 30,
        "printType": "BOOK",
        "maturityRating": "NOT_MATURE",
        "allowAnonLogging": false,
        "contentVersion": "1.1.2.0.full.1",
        "panelizationSummary": {
          "containsEpubBubbles": false,
          "containsImageBubbles": false
        },
        "imageLinks": {
          "smallThumbnail": "http://books.google.com/books/content?id=i5jX0-j_D-QC&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
          "thumbnail": "http://books.google.com/books/content?id=i5jX0-j_D-QC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
        },
        "language": "en",
        "previewLink": "http://books.google.com.vn/books?id=i5jX0-j_D-QC&pg=PA11&dq=galvin&hl=&cd=4&source=gbs_api",
        "infoLink": "https://play.google.com/store/books/details?id=i5jX0-j_D-QC&source=gbs_api",
        "canonicalVolumeLink": "https://play.google.com/store/books/details?id=i5jX0-j_D-QC"
      },
      "saleInfo": {
        "country": "VN",
        "saleability": "FREE",
        "isEbook": true,
        "buyLink": "https://play.google.com/store/books/details?id=i5jX0-j_D-QC&rdid=book-i5jX0-j_D-QC&rdot=1&source=gbs_api"
      },
      "accessInfo": {
        "country": "VN",
        "viewability": "ALL_PAGES",
        "embeddable": true,
        "publicDomain": true,
        "textToSpeechPermission": "ALLOWED",
        "epub": {
          "isAvailable": false,
          "downloadLink": "http://books.google.com.vn/books/download/Galvin_v_Detroit_Steering_Wheel_Windshie.epub?id=i5jX0-j_D-QC&hl=&output=epub&source=gbs_api"
        },
        "pdf": {
          "isAvailable": false
        },
        "webReaderLink": "http://play.google.com/books/reader?id=i5jX0-j_D-QC&hl=&source=gbs_api",
        "accessViewStatus": "FULL_PUBLIC_DOMAIN",
        "quoteSharingAllowed": false
      },
      "searchInfo": {
        "textSnippet": "... \u003cb\u003eGalvin\u003c/b\u003e — in the presence of Mr. Thaddeus \u003cb\u003eGalvin\u003c/b\u003e . I approved of Mr. \u003cb\u003eGalvin&#39;s\u003c/b\u003e discharge at Mr. Keen&#39;s suggestion . I have sold practically all of my stock . I am a son - in - law of Thaddeus \u003cb\u003eGalvin\u003c/b\u003e and am now on good terms with him&nbsp;..."
      }
    },
    {
      "kind": "books#volume",
      "id": "XDfUCQAAQBAJ",
      "etag": "DaQ6ETWtd0g",
      "selfLink": "https://www.googleapis.com/books/v1/volumes/XDfUCQAAQBAJ",
      "volumeInfo": {
        "title": "Galvin's ``Racing Pawns'' Game and a Well-Ordering of Trees",
        "authors": [
          "Stephen B. Grantham"
        ],
        "publisher": "American Mathematical Soc.",
        "publishedDate": "1985",
        "description": "Galvin showed that white always wins [T:T] and gave an explicit strategy for the case where T is finite. We present his proofs here and then show how to give an explicit strategy in the general case.",
        "industryIdentifiers": [
          {
            "type": "ISBN_13",
            "identifier": "9780821823170"
          },
          {
            "type": "ISBN_10",
            "identifier": "0821823175"
          }
        ],
        "readingModes": {
          "text": false,
          "image": true
        },
        "pageCount": 73,
        "printType": "BOOK",
        "categories": [
          "Mathematics"
        ],
        "maturityRating": "NOT_MATURE",
        "allowAnonLogging": false,
        "contentVersion": "0.1.0.0.preview.1",
        "panelizationSummary": {
          "containsEpubBubbles": false,
          "containsImageBubbles": false
        },
        "imageLinks": {
          "smallThumbnail": "http://books.google.com/books/content?id=XDfUCQAAQBAJ&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
          "thumbnail": "http://books.google.com/books/content?id=XDfUCQAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
        },
        "language": "en",
        "previewLink": "http://books.google.com.vn/books?id=XDfUCQAAQBAJ&pg=PA1&dq=galvin&hl=&cd=5&source=gbs_api",
        "infoLink": "https://play.google.com/store/books/details?id=XDfUCQAAQBAJ&source=gbs_api",
        "canonicalVolumeLink": "https://play.google.com/store/books/details?id=XDfUCQAAQBAJ"
      },
      "saleInfo": {
        "country": "VN",
        "saleability": "FOR_SALE",
        "isEbook": true,
        "listPrice": {
          "amount": 619929,
          "currencyCode": "VND"
        },
        "retailPrice": {
          "amount": 433950,
          "currencyCode": "VND"
        },
        "buyLink": "https://play.google.com/store/books/details?id=XDfUCQAAQBAJ&rdid=book-XDfUCQAAQBAJ&rdot=1&source=gbs_api",
        "offers": [
          {
            "finskyOfferType": 1,
            "listPrice": {
              "amountInMicros": 619929000000,
              "currencyCode": "VND"
            },
            "retailPrice": {
              "amountInMicros": 433950000000,
              "currencyCode": "VND"
            }
          }
        ]
      },
      "accessInfo": {
        "country": "VN",
        "viewability": "PARTIAL",
        "embeddable": true,
        "publicDomain": false,
        "textToSpeechPermission": "ALLOWED",
        "epub": {
          "isAvailable": false
        },
        "pdf": {
          "isAvailable": true,
          "acsTokenLink": "http://books.google.com.vn/books/download/Galvin_s_Racing_Pawns_Game_and_a_Well_Or-sample-pdf.acsm?id=XDfUCQAAQBAJ&format=pdf&output=acs4_fulfillment_token&dl_type=sample&source=gbs_api"
        },
        "webReaderLink": "http://play.google.com/books/reader?id=XDfUCQAAQBAJ&hl=&source=gbs_api",
        "accessViewStatus": "SAMPLE",
        "quoteSharingAllowed": false
      },
      "searchInfo": {
        "textSnippet": "... \u003cb\u003eGalvin\u003c/b\u003e , with some modifications of this game , and with a well - ordering defined in terms of these games . The original \u003cb\u003eGalvin\u003c/b\u003e game is played on a tree T having no infinite branches . A white and a black pawn are placed initially at&nbsp;..."
      }
    }
  ]
}
Beta
0 / 0
used queries
1"""