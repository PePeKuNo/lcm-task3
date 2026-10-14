require 'sinatra'
require 'json'

# НОК через НОД
def lcm(x, y)
  return 0 if x == 0 || y == 0
  (x * y) / x.gcd(y)
end

# Валидация: неотрицательное целое число
def valid_nat?(val)
  val =~ /\A\d+\z/ && val.to_i >= 0
end

get '/bpalij22_gmail_com' do
  content_type 'text/plain; charset=utf-8'

  x = params['x']
  y = params['y']

  unless valid_nat?(x) && valid_nat?(y)
    return 'NaN'
  end

  lcm(x.to_i, y.to_i).to_s
end