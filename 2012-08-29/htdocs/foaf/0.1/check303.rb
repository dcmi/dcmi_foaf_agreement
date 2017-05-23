#!/usr/bin/ruby

# Ruby script to test namespace redirects seem to be in place
# Todo: test via HTTP more carefully, ie. that we actually get a 303
    
require 'test/unit'

class TC_FOAFNSTest < Test::Unit::TestCase
 
attr_accessor :tcount, :rcount, :termlist 

  def setup
    @termlist = []
    check303()
  end
  
  def teardown
    @tcount=nil
    @rcount=nil
    @termlist=nil
  end

  def test_gotroqet
    assert(  `roqet -h` =~ /Beckett/, "Didn't find roqet utility needed for testing")
  end

  def test_plausibly_few
    assert(@termlist.size<500, "Do we really have more than 500 terms?")
  end

  def test_plausibly_many
    assert(@termlist.size>20, "I was expecting more than 20 terms")
  end

  def test_counted_ok
    # puts "XXXXX Size: #{@termlist.size.class} tcount: #{@tcount.class}"
    assert( @termlist.size.to_s == @tcount.to_s, "Ooops I miscounted. Internal counting screwup.")
  end

  def test_got_htaccess
    assert( `grep Redirect .htaccess`, "Couldn't find an htaccess file with redirects")
  end

  def test_count
    if (@termlist.size.to_i != rcount.to_i)
      puts "# Sample .htacess: "
      @termlist.each do |t|
        puts "Redirect 303 /foaf/0.1/#{t} http://xmlns.com/foaf/spec/"
      end
      puts "#end sample. \n\n"
    end 
    assert(@termlist.size.to_i == @rcount.to_i, "Mismatch between terms (#{ @termlist.size }) and number of redirects (#{ @rcount})") 
  end

  def test_httpok
    ok=true
    oops=""
    require 'net/http'     
    @termlist.each do |t|
       url = URI.parse('http://xmlns.com/foaf/0.1/'+t)
       req = Net::HTTP::Get.new(url.path)
       res = Net::HTTP.new(url.host, url.port).start {|http| http.request(req) }
       case res
       when Net::HTTPSuccess, Net::HTTPRedirection
       else
         ok=false
         oops += "Error with URL: #{url}"
#         res.error!
       end
    end
    assert(ok, "Had HTTP trouble. " + oops)
  end


  def test_http_nonsense
    require 'net/http'     
    oops=""
    ok=true
    url = URI.parse('http://xmlns.com/foaf/0.1/qwertyuiop')
    req = Net::HTTP::Get.new(url.path)
    res = Net::HTTP.new(url.host, url.port).start {|http| http.request(req) }
    case res
    when Net::HTTPSuccess, Net::HTTPRedirection
        ok=false
        oops += "Error with URL: #{url}"
    end
    assert(ok, "Had HTTP trouble. A nonsense URL worked OK. " + oops)
  end
   


  # we should run this stuff once ... hmm
  #
  def check303 
    terms = `roqet -e 'SELECT * FROM <http://xmlns.com/foaf/0.1/index.rdf> WHERE { ?x <http://www.w3.org/2000/01/rdf-schema#isDefinedBy>     <http://xmlns.com/foaf/0.1/> }' `
     terms =~ /turned (\d*) results/
     @tcount = $1
     @rcount =  `grep Redirect .htaccess  | grep -v '^#' | wc  --lines`
     terms.each do |t|
       t =~ /1\/(\w*)>\]/
       w= $1
       next unless w =~ /\w/
       @termlist.push(w)
     end
     @termlist.sort!
     @tcount.chomp!
     @rcount.chomp!
   end
end



require 'test/unit/ui/console/testrunner'
Test::Unit::UI::Console::TestRunner.run(TC_FOAFNSTest)
