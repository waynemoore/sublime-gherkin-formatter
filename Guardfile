# A sample Guardfile
# More info at https://github.com/guard/guard#readme

guard :shell do
  watch /.py$/ do |m|

    if system('nosetests --with-yanc')
      n "#{m[0]} all tests passed :)", 'Nosetests', :success
    else
      n "#{m[0]} some tests failed :(", 'Nosetests', :failed
    end

  end
end