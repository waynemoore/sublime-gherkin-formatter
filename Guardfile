# A sample Guardfile
# More info at https://github.com/guard/guard#readme

guard :shell do
  watch /.py$/ do |m|
    n "#{m[0]} changed, running tests", 'Nosetests'

    if system('nosetests')
      n "#{m[0]} all tests passed :)", 'Nosetests', :success
    else
      n "#{m[0]} some tests failed :(", 'Nosetests', :failed
    end

  end
end