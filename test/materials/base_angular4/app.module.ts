<%
import cook_template

ng4_imports = root_obj['NG4_IMPORTS']
%>
{{!cook_template.generate_import_header(root_obj)}}

@NgModule({
  declarations: [
    AppComponent,
  ],
  imports: [
% for ng_obj in ng4_imports:
%   for key in ng_obj.keys():
{{ key }},
%   end
% end
  ],
  providers: [],
 `   bootstrap: [AppComponent]
  })
  export class AppModule { }
