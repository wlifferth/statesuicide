# Suicide, The Holidays and Population Density
Because I have an insatiable need to respond to factoids with more factoids, I retort "Did you know Utah has the fifth highest suicide rate of any state?" My mother, incredulous that anything bad could happen in a place full of mormons, questions my claim.
So like any responsible psuedo-scientific know-it-all I check my sources. The first credible result is from the CDC: in 2012 Utah was 5th in age-adjusted suicides. But that wasn't the most interesting thing on the page. In this happenstatial exploratory data analysis I notice the four above Utah all seem somehow similar. Wyoming, Alaska, Montana, New Mexico.
Sure enough, the four most suicide-prone states are among the six least densely populated states. And the top three suicide states are the bottom three by population desnity. At this point I'm feeling clever, so I want to keep digging. In order to get a better picture I want more, cleaner data.
I'm able to pull suicide data from the CDC and population density data from the US census. I clean up the data, kick out the District of Columbia (it is a mad outlier in terms of population density) and start putzing around with it. A couple minutes later I've made this puppy:
Boom.
On the horizontal axis we have population density; this is people per square miles. On the vertical axis we have suicide; this is suicides per 100,000 people. Each point represents a state, the size of which is dependent upon the state's population. Example: California's point is huge, because California contains a metric heck-ton of people. The line is a 2nd order line of best fit, and the field around it is a 95% confidence interval (that is to say, if we created a new/imaginary state, we could be 95% sure it would fall within that field).
On a very basic level, the trend is pretty clear: the denser the population of a state, the lower incidence of suicide it has. Okay, but why?
It's important to note that all this data is entirely observational. I've selected population density as the explanatory variable, but we didn't randomly make people move to different states and wait to see if them killed themselves. So it's just as valid to argue higher suicide rates cause lower population densities (hey maybe people are running away from Wyoming because of its high rate of suicide) as it is to argue lower population densities cause higher suicides rates. But it makes some intuitive sense to look at it this way--so lets run with it.
Why do states with higher population densities tend to have a lower rate of suicide? A host of things also correlate well with population density; densely populated states tend to be more urban and offer more access to healthcare. They also tend to have stricter gun laws. They also tend to be more politically liberal. But that doesn't mean stricter gun laws or liberalism is saving anyone from suicide per se. The same is true of population density. In the words of that one insufferable stats professor we all had at one point: "correlation does not imply causation."
That being said, there is strong theoretical support for the idea that being around other people can increase well being and reduce the risk of suicidal ideation. And hey, the data seems to support that in a non-rigorous way. So let's stay surrounded.

Want to help fight suicide? Check out the American Foundation for Suicide Prevention at afsp.org; If you or someone you know has experienced thoughts of suicide or self harm call or text the Suicide Prevention hotline at 1-800-273-8255.

Stat Suicide Data (2012, CDC)
https://www.cdc.gov/mmwr/preview/mmwrhtml/mm6345a10.htm

State Population Density (2015, based off 2010 census)
https://en.wikipedia.org/wiki/List_of_U.S._states_by_population_density

State Density Taken from census.gov
https://www.census.gov/2010census/csv/pop_density.csv

State Suicide Density Taken from CDC.gov
https://webappa.cdc.gov/cgi-bin/broker.exe
