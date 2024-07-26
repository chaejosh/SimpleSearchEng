from exa_py import Exa

exa = Exa('01f3ac5b-8cbd-4fff-8147-a9a2b4290b62')

query = input('Search here: ')

response = exa.search(
    query,
    num_results =5,
    type = 'keyword',
    include_domains= ['https://www.tiktok.com'],
    )

for result in response.results:
    print(f'Title: {result.title}')
    print(f'URL: {result.url}')
    print()
#print(response)